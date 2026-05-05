import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from selenium import webdriver
import time
import csv
from urllib.parse import urljoin
from collections import defaultdict
import os
import json


# helper functions

def scrape_celeb_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # table info(season, skin, eye, hair, contrast, best, worst)
    chart = soup.find('table')
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






# set up header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# make request
driver = webdriver.Chrome() # need to load page before scraping
driver.get("https://colormineai.com/celebrity/")
time.sleep(5)  # wait for page to load

# parse HTML content
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# get info from cards

#class stuff
#name = soup.find_all('h3', class_ = 'font-bold text-lg text-brand-dark group-hover:text-brand-primary transition-colors')
#job = soup.find_all('p', class_ = 'text-sm text-stone-600 line-clamp-2')
#job_cat = soup.find_all('div', class_ = 'inline-block px-2 py-1 bg-stone-100 rounded-md text-xs text-stone-600')
#pic = soup.find_all('img', class_='w-full h-full object-cover group-hover:scale-105 transition-transform duration-300')

cards = soup.select("a.group")
data = []
id = 0

for card in cards:
    name = card.select_one("h3.font-bold.text-lg.text-brand-dark.group-hover\\:text-brand-primary.transition-colors")
    job = card.select_one("p.text-sm.text-stone-600.line-clamp-2")
    job_cat = card.select_one("div.inline-block.px-2.py-1.bg-stone-100.rounded-md.text-xs.text-stone-600")
    pic = card.select_one("img.w-full.h-full.object-cover.group-hover\\:scale-105.transition-transform.duration-300")  
    # get info from indiv celeb page
    page_href = card.get("href")
    page_link = urljoin("https://colormineai.com", page_href)
    info_table = scrape_celeb_page(page_link)
    # error handling
    if not name or not job or not job_cat:
        continue
    best_color_list = [x.strip() for x in info_table["best_colors"].split(",")]
    worst_color_list = [x.strip() for x in info_table["colors_to_avoid"].split(",")]
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




# close driver
driver.quit()

# to json
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












