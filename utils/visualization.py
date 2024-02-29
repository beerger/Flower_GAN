import os
import matplotlib.pyplot as plt
from PIL import Image
import random

def visualize_n_images(image_dir, rows=1, cols=5, use_random=True):
    """
    Visualizes n images located in given image directory
    
    Parameters:
    - image_dir: Directory that contains the images.
    - rows, cols: The layout of the subplot grid.
    - use_random: If false it uses the first rows * cols \\
              images located in image_dir.
    """

    file_paths = []
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Add or remove file formats as needed
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    num_images = rows * cols
    if use_random and len(file_paths) >= num_images:
        # Randomly select `num_images` from the list of file paths
        selected_paths = random.sample(file_paths, num_images)
    else:
        # If not enough images or `use_random` is False, take the first `num_images`
        selected_paths = file_paths[:num_images]

    fig, axes = plt.subplots(rows, cols, figsize=(20, 4))
    axes = axes.flatten()

    for img_path, ax in zip(selected_paths, axes):
        img = Image.open(img_path)
        ax.imshow(img)
        ax.axis('off')

    plt.tight_layout()
    plt.show()