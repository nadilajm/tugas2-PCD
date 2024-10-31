import numpy as np
import imageio.v3 as imageio
import matplotlib.pyplot as plt

def load_image(image_path):
    """Load image from the specified path."""
    return imageio.imread(image_path)

def grayscale_image(image):
    """Convert the image to grayscale."""
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

# Paths to each image
images = {
    "Daun Pepaya": "daun_pepaya.jpg",
    "Daun Singkong": "daun_singkong.jpg",
    "Daun Kenikir": "daun_kenikir.jpg"
}

# Process each image and display the grayscale version
for name, path in images.items():
    image = load_image(path)
    grayscale = grayscale_image(image)

    plt.figure(figsize=(3, 3))
    plt.imshow(grayscale, cmap='gray')
    plt.title(f"{name} - Grayscale")
    plt.axis('off')
    plt.show()
