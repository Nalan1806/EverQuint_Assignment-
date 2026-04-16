# CIFAR-10 Image Classification using CNN (PyTorch)

## Overview

In this project, I built a Convolutional Neural Network (CNN) from scratch using PyTorch to classify images from the CIFAR-10 dataset. The goal was to implement a complete deep learning pipeline including data preprocessing, model design, training, evaluation, and performance improvement.

---

## Project Structure

```
cifar-10/
│
├── data/              # dataset (auto-generated)
├── evaluate.py  # Model evaluation (test accuracy + misclassified images)
├── model.py    # CNN architecture definition
├── model.pth
├── train.py   # Training pipeline (training loop + early stopping + plots)
├── utils.py     # Data loading and preprocessing
├── requirements.txt
├── README.md
```

---

## Training Setup

* Framework: PyTorch
* Dataset: CIFAR-10
* Batch size: 64
* Optimizer: Adam
* Learning rate: 0.001
* Loss function: CrossEntropyLoss
* Scheduler: StepLR (reduces learning rate every 5 epochs)
* Epochs: Up to 10 (with early stopping)

### Data Preprocessing

* Normalization applied to all images
* Data augmentation:

  * Random horizontal flip
  * Random cropping

These help improve generalization and robustness of the model.

---

## Model Design Decisions

I implemented a custom CNN from scratch instead of using a pre-trained model, as required.

### Architecture Highlights:

* 3 Convolutional layers (increasing depth: 32 → 64 → 128)
* Batch Normalization after each convolution layer for stable training
* MaxPooling layers for spatial downsampling
* Dropout (0.5) to reduce overfitting
* Fully connected layers for classification

### Design Reasoning:

* Increasing channels helps capture more complex features
* BatchNorm improves convergence and training stability
* Dropout prevents overfitting
* A simple architecture was chosen to balance performance and efficiency

---

## Training Approach

The training loop includes:

* Forward pass
* Loss computation
* Backpropagation
* Weight updates using Adam optimizer
* Accuracy tracking per epoch

### Improvement Implemented

I implemented **Early Stopping** as a training utility:

* Training stops if loss does not improve for a fixed number of epochs (patience = 3)
* This prevents overfitting and unnecessary computation

The model checkpoint is saved whenever the best loss is achieved.

---

## Evaluation

The model is evaluated on the test dataset using:

* Test accuracy
* Visualization of misclassified images

### Observations:

* The model achieves ~70% accuracy on CIFAR-10
* Misclassifications often occur between visually similar classes (e.g., airplane vs ship), indicating limitations in feature discrimination

---

## How to Run the Code

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Train the model

```
python train.py
```

This will:

* Train the model
* Save the best model as `model.pth`
* Display loss and accuracy plots

### 3. Evaluate the model

```
python evaluate.py
```

This will:

* Load the trained model
* Compute test accuracy
* Display misclassified images

---

## Limitations & Future Improvements

* The model is relatively simple and can be improved using deeper architectures or residual connections
* Early stopping currently monitors training loss instead of validation loss
* Hyperparameter tuning (learning rate, batch size, dropout) could improve performance
* Using transfer learning or pretrained models could significantly boost accuracy

---

## Conclusion

This project demonstrates a complete deep learning workflow from data preprocessing to evaluation. I focused on writing clean, modular code and implementing best practices such as early stopping and structured evaluation.

---
