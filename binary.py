import numpy as np
import imageio.v3 as imageio
import matplotlib.pyplot as plt

def load_image(image_path):
    """Load image from the specified path."""
    return imageio.imread(image_path)

def binary_threshold(image, threshold):
    """Apply binary thresholding to the image."""
    binary_image = (image > threshold).astype(np.uint8) * 255
    return binary_image

# Paths to each image
images = {
    "Daun Pepaya": "daun_pepaya.jpg",
    "Daun Singkong": "daun_singkong.jpg",
    "Daun Kenikir": "daun_kenikir.jpg"
}

# Process each image and display the binary thresholded version
for name, path in images.items():
    image = load_image(path)
    grayscale = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])  # Convert to grayscale
    binary_image = binary_threshold(grayscale, 128)  # Apply binary thresholding

    plt.figure(figsize=(3, 3))
    plt.imshow(binary_image, cmap='gray')
    plt.title(f"{name} - Binary Thresholded")
    plt.axis('off')
    plt.show()