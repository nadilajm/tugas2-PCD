import imageio as img
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the image
image = img.imread('daun_singkong.jpg')

# Step 2: Check the shape of the image
# The image shape will be (height, width, 3) for RGB images
print("Image shape:", image.shape)


image[:, :, 0] = 0    
image[:, :, 2] = 0  

# Step 4: Display the channels separately using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 1, 1)
plt.title("Green Channel")
plt.imshow(image, cmap="Greens")


plt.show()
