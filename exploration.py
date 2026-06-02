import matplotlib.pyplot as plt
import pandas as pd
import os
from html2image import Html2Image


# get data
base = os.path.abspath(os.path.join(os.path.dirname(__file__)))
filepath_csv = os.path.join(base, "data", "processed", "processed.csv")
df = pd.read_csv(filepath_csv)

list_season = df['season'].value_counts().index.tolist()
list_counts = df['season'].value_counts().values.tolist()

# best color in season
bar_colors = []
for season in list_season:
  season_colors = []
  for i in range(5):
    col_name = f"best_color{i+1}"
    season_colors = season_colors + df[df['season'] == season][col_name].tolist()
  season_colors = pd.Series(season_colors)
  col = season_colors.value_counts().index.tolist()[0]
  bar_colors.append(col)
fig, ax = plt.subplots(figsize = (20, 6))
ax.bar(list_season, list_counts, color = bar_colors)
ax.set_title("Season Counts by Most Recommended Color")
ax.set_xlabel("Season")
ax.set_ylabel("Frequency")
fig.savefig("visualizations/seasons_dist.png")

# distribution of jobs
labels = df['job_short'].value_counts().index.tolist()
values = df['job_short'].value_counts().values.tolist()
colors = ["#9152c9" if label == "Asian Celebrities" else "#4bacc6" for label in labels]

fig, ax = plt.subplots(figsize=(20, 6))
ax.bar(labels, values, color=colors)
ax.set_title("Counts by Job Category")
ax.set_xlabel("Job Category")
ax.set_ylabel("Frequency")
fig.savefig("visualizations/job_dist.png")

# best and worst colors by season
result = []

for season in df['season'].unique():
    subset = df[df['season'] == season]

    most_freq_best1  = subset['best_color1'].mode(dropna=True)
    most_freq_best2  = subset['best_color2'].mode(dropna=True)
    most_freq_worst1 = subset['worst_color1'].mode(dropna=True)
    most_freq_worst2 = subset['worst_color2'].mode(dropna=True)

    result.append({
        "season": season,
        "best_color1": most_freq_best1.iloc[0] if not most_freq_best1.empty else None,
        "best_color2": most_freq_best2.iloc[0] if not most_freq_best2.empty else None,
        "worst_color1": most_freq_worst1.iloc[0] if not most_freq_worst1.empty else None,
        "worst_color2": most_freq_worst2.iloc[0] if not most_freq_worst2.empty else None,
    })

result_df = pd.DataFrame(result)
def color_background(val):
    if pd.isna(val):
        return ""
    
    # Normalize hex to lowercase for safety
    v = str(val).lower().strip()
    
    # If background is white, use black text
    if v == "#ffffff" or v == "white":
        return "background-color: #ffffff; color: black;"
    
    # Otherwise use white text for contrast
    return f"background-color: {val}; color: white;"


styled = (
    result_df.style
        .map(color_background, subset=[
            "best_color1",
            "best_color2",
            "worst_color1",
            "worst_color2"
        ])
        .set_properties(**{"text-align": "center"})
)

os.makedirs("visualizations", exist_ok=True)
html_path = "visualizations/season_colors_table.html"
png_path  = "visualizations/season_colors_table.png"

html = styled.to_html()
with open(html_path, "w") as f:
    f.write(html)

hti = Html2Image()
hti.screenshot(
    html_file=html_path,
    save_as=os.path.basename(png_path),  # filename only
    size=(1200, 600)
)
os.replace(os.path.basename(png_path), png_path)

