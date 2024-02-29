# config.py

# Paths
RAW_DATA_DIR = './data/raw'
PROCESSED_DATA_DIR = './data/processed'
CHECKPOINTS_DIR = ''
RESULTS_DIR = ''

# Preprocessing
TARGET_IMAGE_SIZE = (256, 256)
IMAGE_FORMAT = 'RGB'

# Training
BATCH_SIZE = 64
LEARNING_RATE = 0.0002
EPOCHS = 200
NOISE_DIM = 100  # Dimensionality of the input noise vector for the generator

# Model Architecture Specifics

# GAN Generator
GENERATOR_FEATURES = 64

# GAN Discriminator
DISCRIMINATOR_FEATURES = 64

# Other configurations
SAVE_CHECKPOINT_EVERY_N_EPOCHS = 5
SAMPLE_IMAGES_EVERY_N_EPOCHS = 1
