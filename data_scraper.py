import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import random
import os
import json

base_url = "https://colormineai.com/"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
})
last_request_time = 0
min_request_interval = 1

robots = RobotFileParser()
robots.set_url('https://colormineai.com/robots.txt')
robots.read()


# helper functions
def rate_limit():
    """Ensure we do not exceed rate limits"""
    global last_request_time
    elapsed = time.time() - last_request_time
    wait_time = min_request_interval - random.uniform(0.2, 0.8)
    if elapsed < wait_time:
        time.sleep(wait_time - elapsed)
    last_request_time = time.time()

def check_robots_txt(url: str) -> bool:
    "Check if robots.txt allows scraping"
    path = urlparse(url).path
    return robots.can_fetch(session.headers['User-Agent'], path)

def scrape_celeb_page(url, driver):
    """Scrape information from individual celebrity pages"""
    rate_limit()

    if not check_robots_txt(url):
        return {'url': url, 'error': "Robots.txt does not allow scraping"}
 
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # table info(season, skin, eye, hair, contrast, best, worst)
    chart = soup.find('table')
    driver.quit()
    if not chart:
        return {"url": url, "error": "no table"}
    data = {}
    for row in chart.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) >= 2:
            key = cells[0].get_text(strip = True).lower().replace(" ", "_")
            value = cells[1].get_text(strip = True).lower()
            data[key] = value
    data["url"] = url
    return data

def scrape_main_page(url):
    """Scrape card information from main page"""
    if not check_robots_txt(url):
        return "Cannot scrape this site"
    driver = webdriver.Chrome() # need to load page before scraping
    driver.get(urljoin(url, "celebrity/"))
    time.sleep(5)  # wait for page to load
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    cards = soup.select("a.group")
    data = []
    id = 0
    for card in cards:
        name = card.select_one("h3.font-bold.text-lg.text-brand-dark.group-hover\\:text-brand-primary.transition-colors")
        job = card.select_one("p.text-sm.text-stone-600.line-clamp-2")
        job_cat = card.select_one("div.inline-block.px-2.py-1.bg-stone-100.rounded-md.text-xs.text-stone-600")
        pic = card.select_one("img.w-full.h-full.object-cover.group-hover\\:scale-105.transition-transform.duration-300")  
            
        # error handling
        if not name or not job or not job_cat:
            continue
        # get info from indiv celeb page
        page_href = card.get("href")
        page_link = urljoin(base_url, page_href)
        info_table = scrape_celeb_page(page_link, driver)
        if not info_table:
            continue
        best_color_list = [x.strip() for x in info_table["best_colors"].split(",")]
        if len(best_color_list) < 5:
            best_color_list += [None] * (5 - len(best_color_list))
        worst_color_list = [x.strip() for x in info_table["colors_to_avoid"].split(",")]
        if len(worst_color_list) < 5:
            worst_color_list += [None] * (5 - len(worst_color_list))
        # put all info together
        card_info = {
            "id": id,
            "name": name.text.strip(),
            "job": job.text.strip(),
            "job_cat": job_cat.text.strip(),
            "pic_url": pic['src'] if pic else None,
            "season": info_table['color_season'],
            "skin_tone": info_table['skin_tone'],
            "eye_color": info_table['eye_color'],
            "hair_color": info_table['hair_color'],
            "contrast_level": info_table["contrast_level"],
            "best_color1": best_color_list[0],
            "best_color2": best_color_list[1],
            "best_color3": best_color_list[2],
            "best_color4": best_color_list[3],
            "best_color5": best_color_list[4],
            "worst_color1": worst_color_list[0],
            "worst_color2": worst_color_list[1],
            "worst_color3": worst_color_list[2],
            "worst_color4": worst_color_list[3],
            "worst_color5": worst_color_list[4]
        }  
        data.append(card_info)
        id += 1
    driver.quit()
    return data

    
data = scrape_main_page(base_url)
file = {d["id"]: d for d in data}
os.makedirs("data/raw", exist_ok=True)
with open("data/raw/scraped.json", "w", encoding="utf-8") as f:
    json.dump(file, f, indent=2, ensure_ascii=False)

# part b: to csv
output_path = "data/raw/scraped.csv"

with open(output_path, "w", encoding = "utf-8", newline = "") as f:
    writer = csv.DictWriter(f, fieldnames = data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    