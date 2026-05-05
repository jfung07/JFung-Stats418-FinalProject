import matplotlib.pyplot as plt
import pandas as pd
import os

# get data
base = os.path.abspath(os.path.join(os.path.dirname(__file__)))
filepath_csv = os.path.join(base, "data", "processed", "processed.csv")
df = pd.read_csv(filepath_csv)

list_season = df['season'].value_counts().index.tolist()
list_counts = df['season'].value_counts().values.tolist()

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
fig.savefig("visuals/seasons_dist.png")

labels = df['job_short'].value_counts().index.tolist()
values = df['job_short'].value_counts().values.tolist()
colors = ["#9152c9" if label == "Asian Celebrities" else "#4bacc6" for label in labels]

fig, ax = plt.subplots(figsize=(20, 6))
ax.bar(labels, values, color=colors)
ax.set_title("Counts by Job Category")
ax.set_xlabel("Job Category")
ax.set_ylabel("Frequency")
fig.savefig("visuals/job_dist.png")
