import os
from PIL import Image
import numpy as np
import config


def preprocess_images(raw_data_dir, processed_data_dir, target_size, image_format):
    """
    Preprocesses the images found in the raw data directory and saves them to the processed data directory.
    
    This function will resize each image to the target size, convert it to the specified image format,
    normalize pixel values, and save the image in the processed data directory while preserving the
    directory structure of the raw data directory.

    Args:
        raw_data_dir (str): The directory path that contains the raw images.
        processed_data_dir (str): The directory path where the processed images will be saved.
        target_size (tuple): A tuple (width, height) representing the target image size.
        image_format (str): The desired image format for output (e.g., 'RGB').
    """
    
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
    
    for root, dirs, files in os.walk(raw_data_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Add or remove file formats as needed
                # Construct the path to the image
                file_path = os.path.join(root, file)
                
                # Open the image
                with Image.open(file_path) as img:
                    # Resize the image
                    img = img.resize(target_size, Image.ANTIALIAS)
                    # Convert to the desired format, e.g., RGB
                    img = img.convert(image_format)
                    # Normalize pixel values
                    img = np.asarray(img) / 255.0
                    # Construct the path to save the processed image
                    relative_path = os.path.relpath(file_path, raw_data_dir)
                    processed_path = os.path.join(processed_data_dir, relative_path)
                    processed_dir = os.path.dirname(processed_path)
                    
                    # Create the directory if it doesn't exist
                    if not os.path.exists(processed_dir):
                        os.makedirs(processed_dir)
                    
                    # Save the processed image
                    img.save(processed_path)

# Include a main block to call the preprocessing function
if __name__ == "__main__":
    preprocess_images(config.RAW_DATA_DIR, config.PROCESSED_DATA_DIR, config.TARGET_IMAGE_SIZE, config.IMAGE_FORMAT)