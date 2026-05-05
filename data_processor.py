import pandas as pd
import os

base = os.path.abspath(os.path.join(os.path.dirname(__file__)))
filepath_csv = os.path.join(base, "data", "raw", "scraped.csv")
df_raw = pd.read_csv(filepath_csv)
df_clean = df_raw.copy()

# Missing values
print("Missing values per column: ")
for col in df_clean.columns: 
    missing_vals = sum(df_clean[col].isna())
    print(f"{col}: {missing_vals}")
print("All missing values are in the pics_url column.")

# rows with missing values
print(df_clean[pd.isnull(df_clean['pic_url'])])

# Carli Bybel
df_clean.loc[3, "pic_url"] = "https://ilarge.lisimg.com/image/13751134/740full-carli-bybel.jpg"
# Choi Siwon
df_clean.loc[4, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/d/d9/240813_Choi_Si-won.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Gigi Gorgeous(broken link 404)
df_clean.loc[5, "pic_url"] = "https://www.hawtcelebs.com/wp-content/uploads/2023/06/gigi-gorgeous-at-30th-annual-race-to-erase-ms-gala-in-los-angeles-06-01-2023-0.jpg"
# Hyuna
df_clean.loc[8, "pic_url"] = "https://iv1.lisimg.com/image/25805381/740full-hyuna.jpg"
# Michael Phelps(broken link 404)
df_clean.loc[5, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/c/c7/Michael_Phelps_Rio_Olympics_2016.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Mino
df_clean.loc[11, "pic_url"] = "https://idolinsights.com/wp-content/uploads/2024/06/mino-of-winner.webp"
# Hirai Momo
df_clean.loc[12, "pic_url"] = "https://ilarge.lisimg.com/image/26313724/740full-hirai-momo.jpg"
# Alexander Wang
df_clean.loc[18, "pic_url"] = "https://mercht.com/wp-content/uploads/2025/11/Alexander_Wang_90kb.jpg"
# Desi Perkins
df_clean.loc[22, "pic_url"] = "https://www.hawtcelebs.com/wp-content/uploads/2024/11/desi-perkins-at-l-oreal-paris-s-annual-women-of-worth-celebration-event-in-los-angeles-11-21-2024-3.jpg"
# Jeon Jungkook
df_clean.loc[31, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/4/4c/Jeon_Jung-kook_at_a_fansigning_in_Sinchon%2C_11_December_2015_03.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Lisa
df_clean.loc[33, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/20240314_Lisa_Manoban_07.jpg/330px-20240314_Lisa_Manoban_07.jpg"
# Choi Minho
df_clean.loc[37, "pic_url"] = "https://peliculas.lavanguardia.com/imagenes/w1280/f0YTMge22aY64NDaGnXVeyvowOR.jpg"
# Valentino Garavani
df_clean.loc[40, "pic_url"] = "https://cdn.britannica.com/77/199177-050-7843D61F/Valentino-2009.jpg"
# Dara
df_clean.loc[50, "pic_url"] = "https://images6.fanpop.com/image/photos/32200000/dara-2ne1-lonely-dara-2ne1-32242672-800-1200.jpg"
# Rosalia
df_clean.loc[70, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/3/31/Rosalia_2019-portrait.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Samantha Ravndahl
df_clean.loc[71, "pic_url"] = "https://insanebiography.com/wp-content/uploads/ssssamanthaa_135278730_313260196675050_6809398211726879699_n-min-768x797.jpg"
# Tati Westbrook
df_clean.loc[75, "pic_url"] = "https://wallpapercat.com/w/full/a/0/d/1022741-1152x2048-iphone-hd-tati-westbrook-background-image.jpg"
# Crown Princess Mary of Denmark
df_clean.loc[89, "pic_url"] = "https://i.pinimg.com/originals/18/4a/81/184a81da588bbf8611e1c8ba18758d87.jpg"
# Nyma Tang
df_clean.loc[150, "pic_url"] = "https://media.essence.com/vxcjywbwpa/uploads/2019/12/Nyma.jpg"
# Chloe Morello
df_clean.loc[164, "pic_url"] = "https://www.beautyindependent.com/wp-content/uploads/2022/08/rsz_sireni43123-683x1024.jpg"
# Patricia Bright
df_clean.loc[180, "pic_url"] = "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/patricia-bright_61RG2V3.max-1500x1500.jpg"
# Sasha Banks
df_clean.loc[183, "pic_url"] = "https://i.pinimg.com/originals/a0/ef/e8/a0efe8d41e94c8dca1d81525741fd770.jpg"
# Sooyoung
df_clean.loc[184, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/c/c8/Choi_Sooyoung_LONGCHAMP_2024.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Suga/Min yoongi
df_clean.loc[185, "pic_url"] = "https://i.pinimg.com/originals/f2/93/b1/f293b1020ecfe097261136cc4a1449cd.png"
# Park jimin
df_clean.loc[198, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/8/83/Park_Jimin_at_the_White_House%2C_May_31%2C_2022.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Lisa Eldridge
df_clean.loc[200, "pic_url"] = "https://fashionista.com/.image/t_share/MTI3MjAyNDgwODkwMTE0MDE4/mti1ndkxnji4nze3njq4nte1jpg.jpg"
# Princess Charlotte
df_clean.loc[204, "pic_url"] = "https://ilarge.lisimg.com/image/27250764/740full-princess-charlotte-of-wales.jpg"
# RachhLoves
df_clean.loc[206, "pic_url"] = "https://fresherpost.com/wp-content/uploads/2020/08/Rachel-Cooper-profile.jpg"
# Yuna
df_clean.loc[125, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/5/5b/Yuna_at_Incheon_Airport_on_September_22%2C_2025.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# IU/Lee jieun
df_clean.loc[221, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/7/72/IU_Estee_Lauder_Photo_Call%2C_August_7%2C_2024.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Taylor hill
df_clean.loc[237, "pic_url"] = "https://www.hawtcelebs.com/wp-content/uploads/2024/01/taylor-hill-at-81st-annual-golden-globe-awards-in-los-angeles-01-07-2024-0.jpg"
# Shayla Mitchell
df_clean.loc[254, "pic_url"] = "https://www.lifeandstylemag.com/wp-content/uploads/2019/10/Shayla-Mitchell.png?fit=400%2C499"
# Alessandro Michele
df_clean.loc[258, "pic_url"] = "https://www.usmagazine.com/wp-content/uploads/2022/11/Alessandro-Michele-Leaving-Gucci-0001.jpg?w=1200&quality=86&strip=all"
# KathleenLights
df_clean.loc[263, "pic_url"] = "https://healthyceleb.com/wp-content/uploads/2019/12/KathleenLights-in-an-Instagram-post-as-seen-in-November-2019.jpg"
# Aaliyah Jay
df_clean.loc[269, "pic_url"] = "https://images.squarespace-cdn.com/content/v1/66a7bb7c329d3635d033b603/eb26abd8-f041-45e5-bbd2-83d1c5ef5229/aaliyah-jay-2.jpg"
# Dulce Candy
df_clean.loc[276, "pic_url"] = "https://media.allure.com/photos/57719d5d2554df47220a5be6/3:4/w_767/beauty-trends-blogs-daily-beauty-reporter-2014-05-15-dulce-candy-ruiz.jpg"
# Kai/kim jongin
df_clean.loc[286, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/b/b1/Kai_at_EXO%27luXion_in_Hong_Kong_on_August_16%2C_2015_%282%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Kai/kim jongin
df_clean.loc[286, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/b/b1/Kai_at_EXO%27luXion_in_Hong_Kong_on_August_16%2C_2015_%282%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# IU
df_clean.loc[221, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/7/72/IU_Estee_Lauder_Photo_Call%2C_August_7%2C_2024.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Lauren Curtis
df_clean.loc[317, "pic_url"] = "https://www.gluwee.com/wp-content/uploads/2023/04/Lauren-Curtis-5.jpg"

# Combine job categories and categories to one title   
mapping = {
    "Royal Family Members/Public Figures": "Public Figures",
    "Hollywood Actresses": "Hollywood Actors",
    "Athletes/Sports Figures": "Sports Figures",
    "Fashion Designers/Style Icons": "Style Icons",
    "Historical/Classic Hollywood Icons": "Classic Hollywood Icons",
    "K-pop/Asian Celebrities": "Asian Celebrities",
    "Models/Supermodels": "Models",
    "Musicians/Singers": "Musicians",
    "Social Media Influencers/Content Creators": "Content Creators",
    "TV Personalities/Talk Show Hosts": "TV Personalities"
}

df_clean['job_short'] = df_raw['job_cat'].replace(mapping)


# eye color to brown, blue, green, hazel
eye_color_options = ["brown", "blue", "green", "hazel", "violet"]
def color_match(scrape_color, colors):
    s = str(scrape_color)
    positions = [(c, s.find(c)) for c in colors]
    positions = [(c, pos) for c, pos in positions if pos != -1]
    # cat color does not exist
    if not positions:
        return scrape_color
    return min(positions, key=lambda x: x[1])[0]

df_clean['eye_cat'] = df_raw['eye_color'].apply(lambda x: color_match(x, eye_color_options)) 

# hair color to brown, blonde, black, greyscale, red
hair_color_options = ['dark brown', 'light brown', 'black', 'blonde', 'brunette', 'blond', 'auburn', 'red', 'ginger', 'chestnut', 'salt and pepper', 'grey', 'white', 'brown']
df_clean['hair_cat'] = df_raw['hair_color'].apply(lambda x: color_match(x, hair_color_options))
hair_group = {
    'light brown': ['light brown', 'chestnut', 'brown'],
    'dark brown': ['dark brown', 'brunette'],
    'blonde': ['blonde', 'blond'],
    'red': ['red', 'ginger', 'auburn'],
    'greyscale': ['grey', 'white', 'salt and pepper']
}
hair_lookup = { # flatten to dictionary without groups
    raw.lower(): canonical
    for canonical, variants in hair_group.items()
    for raw in variants
}
df_clean['hair_cat'] = df_clean['hair_cat'].replace(hair_lookup)

df_clean['skin_tone'] = df_raw['skin_tone'].replace("neutral", "warm")

# save clean data
os.makedirs("data/processed", exist_ok=True)
output_path = "data/processed/processed.csv"
df_clean.to_csv(output_path, index = False, encoding = "utf-8")




