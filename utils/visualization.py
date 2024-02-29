import os
import matplotlib.pyplot as plt
from PIL import Image
import random


def visualize_n_images(images=None, image_dir=None, rows=1, cols=5, use_random=True):
    """
    Visualizes n images either located in given image directory, 
    or in given list of PIL images
    
    Precondition: Can only pass either images or image_dir

    Parameters:
    - images: Batch of images to visualize
    - image_dir: Directory that contains the images.
    - rows, cols: The layout of the subplot grid.
    - use_random: If false it uses the first rows * cols 
              images located in image_dir.
    """
    assert (images is None) != (image_dir is None), "Can only pass either images or image_dir, not both"

    if image_dir:
        if not os.path.exists(image_dir):
            raise FileNotFoundError(f"Directory '{image_dir}' does not exist.")

        file_paths = [os.path.join(root, file) for root, _, files in os.walk(image_dir) for file in files
                      if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

        if not file_paths:
            raise ValueError(f"No images found in '{image_dir}'.")

        num_images = rows * cols
        if use_random and len(file_paths) >= num_images:
            selected_paths = random.sample(file_paths, num_images)
        else:
            selected_paths = file_paths[:num_images]
        visual_imgs = [Image.open(img_path) for img_path in selected_paths]
    else:
        visual_imgs = images

    fig, axes = plt.subplots(rows, cols, figsize=(20, 4))
    axes = axes.flatten()
    
    for img, ax in zip(visual_imgs, axes):
        ax.imshow(img)
        ax.axis('off')

    plt.tight_layout()
    plt.show()