from model import CNN
import torch.nn as nn
import torch.optim as optim
import torch 
from utils import get_data_loaders
import matplotlib.pyplot as plt

# Model Initialization

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = CNN().to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Learning rate scheduler
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.5)

train_loader, test_loader = get_data_loaders()

# Training Utility: Early stopping
# stops training if loss does not improve for 'patience' epochs
best_loss = float('inf')
patience = 3
counter = 0

# Training Loop

num_epochs = 10

train_losses = []
train_accuracies = []

for epoch in range(num_epochs):
    model.train()

    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Loss tracking
        running_loss += loss.item()

        # Accuracy tracking
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    # Epoch metrics
    epoch_loss = running_loss / len(train_loader)
    epoch_acc = 100 * correct / total

    # Early stopping logic
    if epoch_loss < best_loss:
        best_loss = epoch_loss
        counter = 0

        # Save BEST model
        torch.save(model.state_dict(), "model.pth")
    else:
        counter += 1

    if counter >= patience:
        print("Early stopping triggered")
        break

    train_losses.append(epoch_loss)
    train_accuracies.append(epoch_acc)

    print(f"Epoch [{epoch+1}/{num_epochs}] Loss: {epoch_loss:.4f} | Accuracy: {epoch_acc:.2f}%")

    # Step scheduler
    scheduler.step()


# Plot Loss
plt.plot(train_losses, label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.legend()
plt.show()

# Plot Accuracy
plt.plot(train_accuracies, label='Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training Accuracy')
plt.legend()
plt.show()