import pandas as pd
import numpy as np
import os
import requests
from PIL import Image
from io import BytesIO

base = os.path.abspath(os.path.join(os.path.dirname(__file__)))
filepath_csv = os.path.join(base, "data", "processed", "processed.csv")
df = pd.read_csv(filepath_csv)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
os.makedirs("images/", exist_ok=True)

# implement rate limiting, but also might be too many requests to the same page, may need to change some urls 

for i in range(len(df.iloc[:,0])):
    filename = f"images/celeb{i}.png"
    url = df['pic_url'][i]
    if not url:
        continue

    r = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
    r.raise_for_status()
    img = Image.open(BytesIO(r.content)).convert("RGB")
    img = img.resize((192, 256)) 
    img.save(filename, format="PNG")






