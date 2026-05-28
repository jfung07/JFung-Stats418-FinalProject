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
# Michael Phelps(broken link 404 -> 400 error need 1280 size)
df_clean.loc[10, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Michael_Phelps_Rio_Olympics_2016.jpg/1280px-Michael_Phelps_Rio_Olympics_2016.jpg"
# Mino
df_clean.loc[11, "pic_url"] = "https://d.kpopstarz.com/en/full/1725582/winner-mino.jpg"
# Hirai Momo
df_clean.loc[12, "pic_url"] = "https://ilarge.lisimg.com/image/26313724/740full-hirai-momo.jpg"
# Sunmi(400 error need 1280 size)
df_clean.loc[16, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/20230720_Lee_Sunmi_on_July_2023_01.jpg/1280px-20230720_Lee_Sunmi_on_July_2023_01.jpg"
# Alexander Wang
df_clean.loc[18, "pic_url"] = "https://media1.popsugar-assets.com/files/thumbor/BRH8dDxl3eJlYD1VXcfsaBAtfyA/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2020/12/31/596/n/1922564/tmp_Gt1ZpQ_f429cb740aee8196_GettyImages-968042892.jpg"
# Desi Perkins
df_clean.loc[22, "pic_url"] = "https://www.hawtcelebs.com/wp-content/uploads/2024/11/desi-perkins-at-l-oreal-paris-s-annual-women-of-worth-celebration-event-in-los-angeles-11-21-2024-3.jpg"
# J balvin(27 404 error)
df_clean.loc[27, "pic_url"] = "https://phantom-elmundo.unidadeditorial.es/e23dea714a0cd81a635fc28123653689/assets/multimedia/imagenes/2022/05/18/16528636693553.jpg"
# Jeon Jungkook
df_clean.loc[31, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/4/4c/Jeon_Jung-kook_at_a_fansigning_in_Sinchon%2C_11_December_2015_03.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Lisa
df_clean.loc[33, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/20240314_Lisa_Manoban_07.jpg/330px-20240314_Lisa_Manoban_07.jpg"
# Choi Minho
df_clean.loc[37, "pic_url"] = "https://peliculas.lavanguardia.com/imagenes/w1280/f0YTMge22aY64NDaGnXVeyvowOR.jpg"
# Valentino Garavani
df_clean.loc[40, "pic_url"] = "https://cdn.britannica.com/77/199177-050-7843D61F/Valentino-2009.jpg"
# Alex Morgan(400 error need 1280 size)
df_clean.loc[41, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Alex_Morgan_May19.jpg/1280px-Alex_Morgan_May19.jpg"
# Anne Hathaway(400 error need 1280 size)
df_clean.loc[43, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Anne_Hathaway_at_The_Apprentice_in_NYC_03_%28cropped2%29.jpg/1280px-Anne_Hathaway_at_The_Apprentice_in_NYC_03_%28cropped2%29.jpg"
# Brie Larson(400 error need 1280 size)
df_clean.loc[46, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Captain_Marvel_trailer_at_the_National_Air_and_Space_Museum_4_%28cropped%29.jpg/1280px-Captain_Marvel_trailer_at_the_National_Air_and_Space_Museum_4_%28cropped%29.jpg"
# Chris Evans(400 error need 1280 size)
df_clean.loc[49, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Chris_Evans_at_the_2025_Toronto_International_Film_Festival_%28cropped%29.jpg/1280px-Chris_Evans_at_the_2025_Toronto_International_Film_Festival_%28cropped%29.jpg"
# Dara
df_clean.loc[50, "pic_url"] = "https://images6.fanpop.com/image/photos/32200000/dara-2ne1-lonely-dara-2ne1-32242672-800-1200.jpg"
# Fred Astaire(400 error need 1280 size)
df_clean.loc[52, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Astaire%2C_Fred_-_Never_Get_Rich.jpg/1280px-Astaire%2C_Fred_-_Never_Get_Rich.jpg"
# Rosalia
df_clean.loc[70, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/3/31/Rosalia_2019-portrait.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Samantha Ravndahl
df_clean.loc[71, "pic_url"] = "https://insanebiography.com/wp-content/uploads/ssssamanthaa_135278730_313260196675050_6809398211726879699_n-min-768x797.jpg"
# Tati Westbrook
df_clean.loc[75, "pic_url"] = "https://wallpapercat.com/w/full/a/0/d/1022741-1152x2048-iphone-hd-tati-westbrook-background-image.jpg"
# Audrey Hepburn(400 error need 1280 size)
df_clean.loc[83, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/AudreyKHepburn.jpg/1280px-AudreyKHepburn.jpg"
# Chloe Kim(88, 404 error)
df_clean.loc[88, "pic_url"] = "https://www.pngmart.com/files/24/Chloe-Kim-Transparent-PNG.png"
# Crown Princess Mary of Denmark
df_clean.loc[89, "pic_url"] = "https://i.pinimg.com/originals/18/4a/81/184a81da588bbf8611e1c8ba18758d87.jpg"
# Henry Cavill(400 error need 1280 size)
df_clean.loc[95, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Henry_Cavill_%2848417913146%29_%28cropped%29.jpg/1280px-Henry_Cavill_%2848417913146%29_%28cropped%29.jpg"
# Mikaela Shiffrin(400 error need 1280 size)
df_clean.loc[110, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Mikaela_Shiffrin_%28Portrait%29.jpg/1280px-Mikaela_Shiffrin_%28Portrait%29.jpg"
# Tyra Banks(400 error need 1280 size)
df_clean.loc[120, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Tyra_Banks_2011.jpg/1280px-Tyra_Banks_2011.jpg"
# Meghan Markle(400 error need 1280 size)
df_clean.loc[145, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/SXSW-2024-OB7A9986-alih-Meghan%2C_Duchess_of_Sussex_%28cropped%29.jpg/1280px-SXSW-2024-OB7A9986-alih-Meghan%2C_Duchess_of_Sussex_%28cropped%29.jpg"
# Nyma Tang
df_clean.loc[150, "pic_url"] = "https://media.essence.com/vxcjywbwpa/uploads/2019/12/Nyma.jpg"
# Oprah Winfrey(400 error need 1280 size)
df_clean.loc[151, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Oprah_Winfrey_2016.jpg/1280px-Oprah_Winfrey_2016.jpg"
# Chloe Morello
df_clean.loc[164, "pic_url"] = "https://www.beautyindependent.com/wp-content/uploads/2022/08/rsz_sireni43123-683x1024.jpg"
# Elizabeth Taylor(400 error need 1280 size)
df_clean.loc[166, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Taylor%2C_Elizabeth_posed.jpg/1280px-Taylor%2C_Elizabeth_posed.jpg"
# Frank Sinatra(400 error need 1280 size)
df_clean.loc[167, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Frank_Sinatra_%281957_studio_portrait_close-up%29.jpg/1280px-Frank_Sinatra_%281957_studio_portrait_close-up%29.jpg"
# Lebron James(400 error need 1280 size)
df_clean.loc[176, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/LeBron_James_%2851959977144%29_%28cropped2%29.jpg/1280px-LeBron_James_%2851959977144%29_%28cropped2%29.jpg"
# Patricia Bright
df_clean.loc[180, "pic_url"] = "https://e5c6t4vikra.exactdn.com/wp-content/uploads/Patricia-Bright-Image-2.jpg"
#  Prince Harry(400 error need 1280 size)
df_clean.loc[181, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Prince_Harry_launching_the_2020_Invictus_Games_%28cropped%29.jpg/1280px-Prince_Harry_launching_the_2020_Invictus_Games_%28cropped%29.jpg"
# Sasha Banks
df_clean.loc[183, "pic_url"] = "https://i.pinimg.com/originals/a0/ef/e8/a0efe8d41e94c8dca1d81525741fd770.jpg"
# Sooyoung
df_clean.loc[184, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/c/c8/Choi_Sooyoung_LONGCHAMP_2024.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Suga/Min yoongi
df_clean.loc[185, "pic_url"] = "https://i.pinimg.com/originals/f2/93/b1/f293b1020ecfe097261136cc4a1449cd.png"
# Zayn Malik(400 error need 1280 size)
df_clean.loc[189, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Zayn_Wiki_%28cropped%29.jpg/1280px-Zayn_Wiki_%28cropped%29.jpg"
# Park jimin
df_clean.loc[198, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/8/83/Park_Jimin_at_the_White_House%2C_May_31%2C_2022.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Lisa Eldridge
df_clean.loc[200, "pic_url"] = "https://fashionista.com/.image/t_share/MTI3MjAyNDgwODkwMTE0MDE4/mti1ndkxnji4nze3njq4nte1jpg.jpg"
# Miley Cyrus(400 error need 1280 size)
df_clean.loc[202, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Miley_Cyrus_Primavera19_-226_%2848986293772%29_%28cropped%29.jpg/1280px-Miley_Cyrus_Primavera19_-226_%2848986293772%29_%28cropped%29.jpg"
# Princess Charlotte
df_clean.loc[204, "pic_url"] = "https://ilarge.lisimg.com/image/27250764/740full-princess-charlotte-of-wales.jpg"
# RachhLoves
df_clean.loc[206, "pic_url"] = "https://fresherpost.com/wp-content/uploads/2020/08/Rachel-Cooper-profile.jpg"
# Sara Jessica Parker(400 error need 1280 size)
df_clean.loc[210, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Sarah_Jessica_Parker_2022.jpg/1280px-Sarah_Jessica_Parker_2022.jpg"
# Yuna
df_clean.loc[215, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/5/5b/Yuna_at_Incheon_Airport_on_September_22%2C_2025.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# IU/Lee jieun
df_clean.loc[221, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/7/72/IU_Estee_Lauder_Photo_Call%2C_August_7%2C_2024.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Rose(wine not celebrity)
df_clean.loc[230, "pic_url"] = "https://celebmafia.com/wp-content/uploads/2024/10/rose-blackpink-siriusxm-portraits-october-2024-0.jpg"
# Taylor hill
df_clean.loc[237, "pic_url"] = "https://www.hawtcelebs.com/wp-content/uploads/2024/01/taylor-hill-at-81st-annual-golden-globe-awards-in-los-angeles-01-07-2024-0.jpg"
# Bianca Andreescu(400 error need 1280 size)
df_clean.loc[239, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Bianca_Andreescu_%282023_DC_Open%29_04_%28cropped%29.jpg/1280px-Bianca_Andreescu_%282023_DC_Open%29_04_%28cropped%29.jpg"
# Camilla, Duchess of Cornwall(400 error need 1280 size)
df_clean.loc[242, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Queen_Camilla_in_Aotearoa_2019.jpg/1280px-Queen_Camilla_in_Aotearoa_2019.jpg"
# Crown Prince Frederik of Denmark(400 error need 1280 size)
df_clean.loc[243, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/King_Frederik_X_in_2025.jpg/1280px-King_Frederik_X_in_2025.jpg"
# Ronda Rousey(400 error need 1280 size)
df_clean.loc[251, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Rousey_HOF_2018_%28cropped%29.jpg/1280px-Rousey_HOF_2018_%28cropped%29.jpg"
# Shayla Mitchell
df_clean.loc[254, "pic_url"] = "https://www.lifeandstylemag.com/wp-content/uploads/2019/10/Shayla-Mitchell.png"
# Tom Brady(400 error need 1280 size)
df_clean.loc[257, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/25th_Laureus_World_Sports_Awards_-_Red_Carpet_-_Tom_Brady_-_240422_191334_%28cropped%29_%28cropped%29.jpg/1280px-25th_Laureus_World_Sports_Awards_-_Red_Carpet_-_Tom_Brady_-_240422_191334_%28cropped%29_%28cropped%29.jpg"
# Alessandro Michele
df_clean.loc[258, "pic_url"] = "https://www.usmagazine.com/wp-content/uploads/2022/11/Alessandro-Michele-Leaving-Gucci-0001.jpg?w=1200&quality=86&strip=all"
# Graham Norton(400 error need 1280 size)
df_clean.loc[261, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/GrahamNorton-byPhilipRomano.jpg/1280px-GrahamNorton-byPhilipRomano.jpg"
# KathleenLights
df_clean.loc[263, "pic_url"] = "https://healthyceleb.com/wp-content/uploads/2019/12/KathleenLights-in-an-Instagram-post-as-seen-in-November-2019.jpg"
# Miyawaki Sakura(400 error need 1280 size)
df_clean.loc[264, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/20241018_Le_Sserafim%27s_Sakura_Miyawaki_04.jpg/1280px-20241018_Le_Sserafim%27s_Sakura_Miyawaki_04.jpg"
# Aaliyah Jay
df_clean.loc[269, "pic_url"] = "https://images.squarespace-cdn.com/content/v1/66a7bb7c329d3635d033b603/eb26abd8-f041-45e5-bbd2-83d1c5ef5229/aaliyah-jay-2.jpg"
# Bruno Mars(400 error need 1280 size)
df_clean.loc[273, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/BrunoMars24KMagicWorldTourLive_%28cropped%29.jpg/1280px-BrunoMars24KMagicWorldTourLive_%28cropped%29.jpg"
# Dulce Candy
df_clean.loc[276, "pic_url"] = "https://media.allure.com/photos/57719d5d2554df47220a5be6/3:4/w_767/beauty-trends-blogs-daily-beauty-reporter-2014-05-15-dulce-candy-ruiz.jpg"
# Kai/kim jongin
df_clean.loc[286, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/b/b1/Kai_at_EXO%27luXion_in_Hong_Kong_on_August_16%2C_2015_%282%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Kai/kim jongin
df_clean.loc[287, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/b/b1/Kai_at_EXO%27luXion_in_Hong_Kong_on_August_16%2C_2015_%282%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
# Rita Hayworth(400 error need 1280 size)
df_clean.loc[296, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Rita_Hayworth_1940s.jpg/1280px-Rita_Hayworth_1940s.jpg"
# IU
df_clean.loc[315, "pic_url"] = "https://upload.wikimedia.org/wikipedia/commons/7/72/IU_Estee_Lauder_Photo_Call%2C_August_7%2C_2024.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original"
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




