"""

Evaluate trained CNN on CIFAR-10 test dataset.

Steps:
- Load trained model
- Load test data
- Compute test accuracy
"""

import torch
from model import CNN
from utils import get_data_loaders


# Device setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model
model = CNN().to(device)
model.load_state_dict(torch.load("model.pth"))
model.eval()  # IMPORTANT


# Load data
_, test_loader = get_data_loaders()


# Evaluation
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)

        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()


accuracy = 100 * correct / total
import matplotlib.pyplot as plt

misclassified = []

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)

        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        for i in range(len(images)):
            if predicted[i] != labels[i]:
                misclassified.append((images[i].cpu(), predicted[i].cpu(), labels[i].cpu()))

        if len(misclassified) >= 5:
            break

# Displaying sample misclassified images
for i in range(5):
    img, pred, true = misclassified[i]

    img = img.permute(1, 2, 0)  # convert to HWC
    img = (img+1)/2
    plt.imshow(img)
    plt.title(f"Pred: {pred} | True: {true}")
    plt.axis('off')
    plt.show()

print(f"Test Accuracy: {accuracy:.2f}%")