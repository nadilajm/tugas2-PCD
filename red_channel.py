import numpy as np
import imageio.v3 as imageio
import matplotlib.pyplot as plt

def load_image(image_path):
    """Load image from the specified path."""
    return imageio.imread(image_path)

def extract_channels(image):
    """Extract R, G, B channels from the image and make each channel stand out."""
    R = image[:, :, 0]
    
    # Highlight channels by zeroing out the others
    R_img = np.stack([R, np.zeros_like(R), np.zeros_like(R)], axis=-1)

    return R_img

# Paths to each image
images = {
    "Daun Pepaya": "daun_pepaya.jpg",
    "Daun Singkong": "daun_singkong.jpg",
    "Daun Kenikir": "daun_kenikir.jpg"
}

# Process each image and display in 1 row with 5 columns
for name, path in images.items():
    image = load_image(path)
    
    # Extract color channels with emphasis on each channel
    R_img = extract_channels(image)
    
    # ... (Your existing code) ...

    # Display only the red channel for each image
    plt.figure(figsize=(3, 3))
    plt.imshow(R_img)
    plt.title(f"{name} - Red Channel")
    plt.axis('on')
    plt.show()