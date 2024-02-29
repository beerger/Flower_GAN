import os
import matplotlib.pyplot as plt
from PIL import Image

def visualize_n_images(image_dir, rows=1, cols=5, random=True):
    """
    Visualizes n images located in given image directory
    
    Parameters:
    - image_dir: Directory that contains the images.
    - rows, cols: The layout of the subplot grid.
    - random: If false it uses the first rows * cols \\
              images located in image_dir.
    """

    fig, axes = plt.subplots(rows, cols, figsize=(20, 4))
    axes = axes.flatten()

    num_images = rows * cols
    image_paths = []
    if random:
        file_paths = []
        for root, dirs, files in os.walk(image_dir):
               for file in files:
                   if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Add or remove file formats as needed
                       # Construct the path to the image
                       file_path = os.path.join(root, file)
                       file_paths.append(file_path)
        indices = random.randrange(num_images)
 
        image_paths = file_paths[indices]                       

    else:
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Add or remove file formats as needed
                    # Construct the path to the image
                    file_path = os.path.join(root, file)
                    image_paths.append(file_path)
                    if(len(image_paths) == num_images):
                        break
    
    for img_path, ax in zip(image_paths, axes):
        with Image.open(img_path) as img:
            if isinstance(img, Image.Image):
                ax.imshow(img)
            else:
                ax.imshow(img, cmap='gray')  # For grayscale images
            ax.axis('off')
    
    plt.tight_layout()
    plt.show()