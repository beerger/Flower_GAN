import os
from PIL import Image, ImageOps
import numpy as np
import config
import torchvision.transforms as transforms
from torchvision.models.detection import fasterrcnn_resnet50_fpn
import torch

# Load a pre-trained Faster R-CNN model
model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()  # Set the model to evaluation mode

# Function to preprocess and perform object detection
def detect_and_crop(img, target_size, threshold=0.5):
    transform = transforms.Compose([transforms.ToTensor()])
    img_tensor = transform(img).unsqueeze(0)
    
    # Perform object detection
    with torch.no_grad():
        prediction = model(img_tensor)
    
    # Filter detection results
    pred_scores = prediction[0]['scores']
    pred_boxes = prediction[0]['boxes']
    max_score_idx = pred_scores.argmax()  # Example: taking the box with the highest score
    print(pred_scores[max_score_idx])
    if pred_scores[max_score_idx] >= threshold:
        box = pred_boxes[max_score_idx].numpy().astype(int)
        cropped_img = img.crop((box[0], box[1], box[2], box[3]))
        img = cropped_img.resize(target_size, Image.LANCZOS)
        return img
    else:
        print("Hello")
        return img  # Return the original image if no high-confidence detections

def center_crop_and_resize(img, target_size):
    """
    Center crops image with size HxH if H < W, WxW if W < H.
    Then resizes image to target size.
    
    Args:
    - img: Image to be cropped and resized
    - target_size: Size of image after resizing

    Returns:
    - Cropped and resizes image
    """
    # Determine the size for cropping
    crop_size = min(img.size)
    
    # Calculate cropping box
    left = (img.width - crop_size) / 2
    top = (img.height - crop_size) / 2
    right = (img.width + crop_size) / 2
    bottom = (img.height + crop_size) / 2
    
    # Crop the center of the image
    img = img.crop((left, top, right, bottom))
    
    # Resize the cropped image to the desired output size
    img = img.resize(target_size, Image.LANCZOS)
    
    return img

def resize_and_pad(img, target_size):
    """
    Adds padding to shorter side to make image square
    
    Args:
    - img: Image to be cropped and resized
    - target_size: Size of image after resizing

    Returns:
    - Resized and padded image
    """
    # Resize while preserving aspect ratio
    img.thumbnail((target_size[0], target_size[1]), Image.LANCZOS)
    
    # Padding
    padding_color = 0  # Example: black padding
    img = ImageOps.expand(img, border=(0, (target_size[1] - img.size[1]) // 2), fill=padding_color)
    img = ImageOps.expand(img, border=((target_size[0] - img.size[0]) // 2, 0), fill=padding_color)
    
    # Ensure the image is exactly the desired output size
    img = img.crop((0, 0, target_size[0], target_size[1]))
    return img


def preprocess_images(raw_data_dir, processed_data_dir, target_size, image_format):
    """
    Preprocesses the images found in the raw data directory and saves them to the processed data directory.
    
    This function will resize each image to the target size, convert it to the specified image format,
    normalize pixel values, and save the image in the processed data directory while preserving the
    directory structure of the raw data directory.

    Args:
        - raw_data_dir (str): The directory path that contains the raw images.
        - processed_data_dir (str): The directory path where the processed images will be saved.
        - target_size (tuple): A tuple (width, height) representing the target image size.
        - image_format (str): The desired image format for output (e.g., 'RGB').
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
                    img = center_crop_and_resize(img, target_size)
                    # Convert to the desired format
                    img = img.convert(image_format)
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