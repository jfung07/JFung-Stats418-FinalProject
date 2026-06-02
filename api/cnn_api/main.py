import os
import io
from fastapi import FastAPI, UploadFile
import torch
from torchvision import transforms
from PIL import Image
from models.cnn import SimpleCNN
from contextlib import asynccontextmanager

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODELS_DIR = os.path.join(ROOT, "models")

@asynccontextmanager
async def lifespan(app: FastAPI):
    cnn_path = os.path.join(MODELS_DIR, "cnn.pth")

    try:
        cnn = SimpleCNN(num_classes=12)
        state = torch.load(cnn_path, map_location="cpu")
        cnn.load_state_dict(state)
        cnn.eval()
        app.state.cnn = cnn
        print("CNN loaded")
    except Exception as e:
        app.state.cnn = None
        print(f"CNN load error: {e}")

    app.state.classes = [
        "cool winter", "cool summer", "warm autumn", "deep autumn",
        "deep winter", "light spring", "light summer", "clear winter",
        "soft autumn", "clear spring", "warm spring", "soft summer"
    ]

    yield
    print("CNN service shutting down")

app = FastAPI(lifespan=lifespan)

@app.get("/ready")
def ready():
    return {"ready": app.state.cnn is not None}

transform = transforms.Compose([
    transforms.Resize((192, 256)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.47972053, 0.41974678, 0.41424349],
        std=[0.27473091, 0.24852708, 0.24372503]
    )
])

@app.post("/predict")
async def predict_image(file: UploadFile):
    img = Image.open(io.BytesIO(await file.read())).convert("RGB")
    tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        outputs = app.state.cnn(tensor)
        idx = torch.argmax(outputs, dim=1).item()

    return {"season": app.state.classes[idx]}
