# packages
import os
import pandas as pd
import shutil
import random



# data
base = os.path.abspath(os.path.join(os.path.dirname(__file__)))
filepath_csv = os.path.join(base, "data", "processed", "processed.csv")
df = pd.read_csv(filepath_csv)
splits = ['train', 'val', 'test']

# delete images folder is it exists
if os.path.exists("data/images"):
    image_dir = 'data/images'


    # collect images
    images = [img for img in os.listdir(image_dir) if img.lower().endswith(".png")]
    random.seed(256)
    random.shuffle(images)

    # split folders
    split_dir = 'data/split'
    for split in splits:
        os.makedirs(os.path.join(split_dir, split), exist_ok = True)
    # 70/15/15
    n = len(images)
    train_end = int(n*0.7)
    val_end = int(n*0.85)
    train_imgs, val_imgs, test_imgs = images[:train_end], images[train_end:val_end], images[val_end:]
    split_mapping = {
        'train': train_imgs,
        'val': val_imgs,
        'test': test_imgs
    }

    # move images into split folders
    for split, img_list in split_mapping.items():
        for img in img_list:
            csv_index = int(img.replace("celeb", "").replace(".png", "").strip())
            label = str(df['season'][csv_index])
            outdir = os.path.join(split_dir, split, label)
            os.makedirs(outdir, exist_ok = True)
            shutil.move(os.path.join(image_dir, img), os.path.join(outdir, img))
    print(f"Split {len(images)} images into train/val/test folders")
    print(f"Train: {len(train_imgs)} images, Val: {len(val_imgs)} images, Test: {len(test_imgs)} images")

    shutil.rmtree("data/images")

# split csv data based on image splits
train_df = pd.DataFrame()
for loc in os.listdir("data/split/train"):
    for celeb in os.listdir(f"data/split/train/{loc}"):
        csv_index = int(celeb.replace("celeb", "").replace(".png", "").strip())
        row = df.loc[csv_index]
        train_df = pd.concat([train_df, row.to_frame().T], ignore_index = True)

val_df = pd.DataFrame()
for loc in os.listdir("data/split/val"):
    for celeb in os.listdir(f"data/split/val/{loc}"):
        csv_index = int(celeb.replace("celeb", "").replace(".png", "").strip())
        row = df.loc[csv_index]
        val_df = pd.concat([val_df, row.to_frame().T], ignore_index = True)

test_df = pd.DataFrame()
for loc in os.listdir("data/split/test"):
    for celeb in os.listdir(f"data/split/test/{loc}"):
        csv_index = int(celeb.replace("celeb", "").replace(".png", "").strip())
        row = df.loc[csv_index]
        test_df = pd.concat([test_df, row.to_frame().T], ignore_index = True)

# save split csv
for split in splits:
    os.makedirs("data/processed", exist_ok=True)
    output_path = f"data/processed/{split}.csv"
    if split == "train":
        train_df.to_csv(output_path, index=False, encoding="utf-8")
    elif split == "val":
        val_df.to_csv(output_path, index=False, encoding="utf-8")
    else:
        test_df.to_csv(output_path, index=False, encoding="utf-8")

