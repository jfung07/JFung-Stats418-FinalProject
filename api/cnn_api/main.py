import os
import io
from flask import Flask, request, jsonify
import torch
from torchvision import transforms
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(ROOT, "models")
from models.cnn import SimpleCNN

CNN_PATH = os.path.join(MODELS_DIR, "cnn.pth")

app = Flask(__name__)

# load model
def load_cnn():
    try:
        cnn = SimpleCNN(num_classes=12)
        state = torch.load(CNN_PATH, map_location="cpu")
        cnn.load_state_dict(state)
        cnn.eval()
        return cnn
    except Exception as e:
        print(f"Error loading CNN: {e}")
        return None

cnn_model = load_cnn()

# need to remove pandas
CLASSES = [
    "cool winter", "cool summer", "warm autumn", "deep autumn",
    "deep winter", "light spring", "light summer", "clear winter",
    "soft autumn", "clear spring", "warm spring", "soft summer"
]

# image transform
transform = transforms.Compose([
    transforms.Resize((192, 256)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.47972053, 0.41974678, 0.41424349],
        std=[0.27473091, 0.24852708, 0.24372503]
    )
])

@app.route("/ready", methods=["GET"])
def ready():
    return jsonify({"ready": cnn_model is not None})

@app.route("/predict", methods=["POST"])
def predict():
    if cnn_model is None:
        return jsonify({"error": "Model not loaded"}), 500
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    img = Image.open(io.BytesIO(file.read())).convert("RGB")
    tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        outputs = cnn_model(tensor)
        idx = torch.argmax(outputs, dim=1).item()
    return jsonify({"season": CLASSES[idx]})
