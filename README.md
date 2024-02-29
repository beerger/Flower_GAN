# Flower_GAN
GAN to generate images of flowers


# Project structure

```flower-gan/
│
├── data/ # Directory for storing the dataset
│ ├── raw/ # Raw, unprocessed data
│ └── processed/ # Preprocessed data ready for model training
│
├── models/ # Model definitions and architecture
│ ├── generator.py # Generator model architecture
│ └── discriminator.py # Discriminator model architecture
│
├── utils/ # Utility scripts for data preprocessing, etc.
│ ├── dataloader.py # Script for loading and preprocessing data
│ ├── visualization.py # Utilities for visualizing images, training progress, etc.
| └── preprocess.py # Script for static preprocessing, resizing, format, normalization
│
├── checkpoints/ # Saved model weights and checkpoints
│
├── results/ # Generated images, model outputs, and evaluation metrics
│
├── train.py # Main script for training the GAN
├── evaluate.py # Script for evaluating the GAN and generating images
│
├── config.py # Configuration file for model parameters, paths, etc.
|
└── main.ipynb # Notebook for training and evaluation
```