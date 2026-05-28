import pandas as pd
import os
import requests
from PIL import Image
from io import BytesIO
import time
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import random

base = os.path.abspath(os.path.join(os.path.dirname(__file__)))
filepath_csv = os.path.join(base, "data", "processed", "processed.csv")
df = pd.read_csv(filepath_csv)
os.makedirs("data/images/", exist_ok=True)

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
last_request_time = 0
min_request_interval = 30


# implement rate limiting, but also might be too many requests to the same page, may need to change some urls
def rate_limit():
    """Ensure we do not exceed rate limits"""
    global last_request_time
    elapsed = time.time() - last_request_time
    wait_time = min_request_interval - random.uniform(0.2, 0.8)
    if elapsed < wait_time:
        time.sleep(wait_time - elapsed)
    last_request_time = time.time()

def get_robots_parser(image_url):
    """Gets RobotFileParser for the domain hosting image"""
    parsed = urlparse(image_url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try: 
        rp.read()
    except:
        return None # there is no robots.txt(assume ok)
    return rp

def check_robots_txt(url: str) -> bool:
    "Check if robots.txt allows scraping"
    rp = get_robots_parser(url)
    if rp is None:
        return True
    path = urlparse(url).path
    return rp.can_fetch(session.headers['User-Agent'], path)


def scrape_image(url, filename):
    """Scrape image from url and save to local directory"""
    if not isinstance(url, str) or not url.startswith("http"):
        raise ValueError(f"Invalid image url: {url}")
    #if not check_robots_txt(url):
        #raise ValueError(f"Robots.txt does not allow scraping of {url}")
    
    rate_limit()
    if not url:
        raise ValueError("Empty URL")
    r = session.get(url,
                     allow_redirects = True,
                     timeout = 10)
    r.raise_for_status()
    img = Image.open(BytesIO(r.content)).convert("RGB")
    img = img.resize((192, 256))
    img.save(filename, format="PNG")


for i in range(len(df.iloc[:,0])):
    filename = f"data/images/celeb{i}.png"
    url = df.iloc[i]["pic_url"]
    try:
        scrape_image(url, filename)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    






