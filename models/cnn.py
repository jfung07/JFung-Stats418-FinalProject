# packages 
# packages
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, ConcatDataset
from torchvision import datasets
import torchvision.transforms as transforms
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
import os
from PIL import Image


torch.manual_seed(256)
np.random.seed(256)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Running on device {device}")

# data 
base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
path_csv = os.path.join(base, "data", "processed", "processed.csv")
df = pd.read_csv(path_csv)
classes = df['season'].value_counts().index.to_list()

# training image normalization data
means = []
stdevs = []
train_img_path = os.path.join(base, "data", "split", "train")
for season in os.listdir(train_img_path):
  for celeb in os.listdir(f"{train_img_path}/{season}"):
    if not celeb.lower().endswith((".png")):
      continue
    path = os.path.join(f"{train_img_path}/{season}/{celeb}")
    img = Image.open(path).convert("RGB")
    arr = np.array(img) / 255.0
    means.append(arr.mean(axis = (0,1)))
    stdevs.append(arr.std(axis = (0,1)))
train_mean = np.mean(means, axis = 0)
train_stdev = np.mean(stdevs, axis = 0)
print(f"Mean: {train_mean} and Stdev: {train_stdev}")

# transforms
train_transform = transforms.Compose([
    transforms.RandomVerticalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(mean = train_mean, std = train_stdev)
])

test_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean = train_mean, std = train_stdev)
])

# transform data
img_path = os.path.join(base, "data", "split")
train_ds = datasets.ImageFolder(os.path.join(img_path, "train"),
                                transform = train_transform)
val_ds = datasets.ImageFolder(os.path.join(img_path, "val"),
                              transform = train_transform)
test_ds = datasets.ImageFolder(os.path.join(img_path, "test"),
                               transform = test_transform)
# add validation into training because not doing hyperparameter search
train_ds = ConcatDataset([train_ds, val_ds])
print(f"Training samples: {len(train_ds)}")
#print(f"Validation samples: {len(val_ds)}")
print(f"Test samples: {len(test_ds)}")

# data loaders
train_loader = DataLoader(train_ds, batch_size = 32, shuffle = True)
#val_loader = DataLoader(val_ds, batch_size = 32, shuffle = False)
test_loader = DataLoader(test_ds, batch_size = 32, shuffle = False)
print(f"Number of training batches: {len(train_loader)}")
#print(f"Number of validation batches: {len(val_loader)}")
print(f"Number of test batches: {len(test_loader)}")

images, labels = next(iter(train_loader))

# model
class SimpleCNN(nn.Module):
  def __init__(self, num_classes = 12):
    super(SimpleCNN, self).__init__()
    # input is 192x256x3 image

    # Block 1: 192x256x3 -> 96x128x32
    self.block1 = nn.Sequential(
        nn.Conv2d(3, 32, kernel_size=3, stride = 2, padding = 1), # (32 filters, 3x3(kernel), padding = 1)
        nn.ReLU(inplace = True), #-> ReLU
    )

    # Block 2: 96x128x32 -> 48x64x64
    self.block2 = nn.Sequential(
        nn.Conv2d(32, 64, kernel_size=3, stride = 2, padding = 1),
        nn.ReLU(inplace = True),
    )

    # Block 3: 48x64x64 -> 24x32x128
    self.block3 = nn.Sequential(
        nn.Conv2d(64, 128, kernel_size=3, stride = 2, padding = 1),
        nn.ReLU(inplace = True),
    )

    # Block 4: 24x32x128 -> 12x16x256
    self.block4 = nn.Sequential(
        nn.Conv2d(128, 256, kernel_size=3, stride = 2, padding = 1),
        nn.ReLU(inplace = True),
    )

    # Flatten Layer 12x16x256 -> 12*16*256
    self.flatten = nn.Flatten()

    # Fully Connected Later: 12*16*256 -> 256
    self.layer1 = nn.Linear(12*16*256, 256)
    self.activation = nn.ReLU()

    # Output Layer: 256 -> 12
    self.classifier = nn.Linear(256, num_classes)

  def forward(self, x):
    x = self.block1(x) # 192x256x3 -> 96x128x32
    x = self.block2(x) # 96x128x32 -> 48x64x64
    x = self.block3(x) # 48x64x64 -> 24x32x128
    x = self.block4(x) # 24x32x128 -> 12x16x256
    x = self.flatten(x) # 12x16x256 -> 12*16*256
    x = self.activation(self.layer1(x))
    x = self.classifier(x)
    return x

# training configuration(testing shows early stopping after 8 epochs is adequate)
model = SimpleCNN(num_classes=12).to(device)
NUM_EPOCHS = 8
LEARNING_RATE = 0.001

# Loss function
criterion = nn.CrossEntropyLoss()

# Optimizer
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# Learning rate scheduler (reduce LR when validation loss plateaus)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='min', factor=0.5, patience=2
)

# training helper functions
def train_one_epoch(model, train_loader, criterion, optimizer, device):
    """Train for one epoch"""
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    all_pred = []
    all_label = []

    for batch_idx, (images, labels) in enumerate(train_loader):
        images, labels = images.to(device), labels.to(device)

        # Zero gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        # Backward pass
        loss.backward()

        # Update weights
        optimizer.step()

        # Statistics
        running_loss += loss.item() * images.size(0)
        _, predicted = outputs.max(1)
        total += labels.size(0)
        correct += predicted.eq(labels).sum().item()
        all_pred.extend(predicted.cpu().numpy())
        all_label.extend(predicted.cpu().numpy())

    epoch_loss = running_loss / total
    epoch_acc = 100. * correct / total
    epoch_f1 = f1_score(all_label, all_pred, average = "macro")
    return epoch_loss, epoch_acc, epoch_f1

def evaluate(model, test_loader, criterion, device):
    """Evaluate the model on test set"""
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    all_pred = []
    all_label = []

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * images.size(0)
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
            all_pred.extend(predicted.cpu().numpy())
            all_label.extend(labels.cpu().numpy())

    epoch_loss = running_loss / total
    epoch_acc = 100. * correct / total
    epoch_f1 = f1_score(all_label, all_pred, average = "macro") 
    return epoch_loss, epoch_acc, epoch_f1

from sklearn.metrics._plot.confusion_matrix import confusion_matrix
def plot_confusion_matrix(model, test_loader, devce, classes):
  model.eval()
  y_pred = []
  y_true = []

  with torch.no_grad():
    for images, labels in test_loader:
      images, labels = images.to(device), labels.to(device)
      outputs = model(images)
      _, predicted = outputs.max(1)

      y_pred.extend(predicted.cpu().numpy())
      y_true.extend(labels.cpu().numpy())

  cm = confusion_matrix(y_true, y_pred)
  return cm

# train
train_losses = []
train_accs = []
test_losses = []
test_accs = []
test_f1s = []

print("Starting training...")
print(f"{'Epoch':<8} {'Train Loss':<12} {'Train Acc':<12} {'Test Loss':<12} {'Test Acc':<12} {'Test f1':<12}")
print("-" * 60)

for epoch in range(NUM_EPOCHS):
    # Train
    train_loss, train_acc, train_f1 = train_one_epoch(model, train_loader, criterion, optimizer, device)

    # Evaluate
    test_loss, test_acc, test_f1 = evaluate(model, test_loader, criterion, device)

    # Update scheduler
    scheduler.step(test_loss)

    # Save metrics
    train_losses.append(train_loss)
    train_accs.append(train_acc)
    test_losses.append(test_loss)
    test_accs.append(test_acc)
    test_f1s.append(test_f1)

    print(f"{epoch+1:<8} {train_loss:<12.4f} {train_acc:<12.2f} {test_loss:<12.4f} {test_acc:<12.2f} {test_f1:<12.2f}")

print("\nTraining complete!") 

# save model to pkl
torch.save(model.state_dict(), "models/cnn_weights.pth")

