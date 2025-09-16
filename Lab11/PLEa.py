import numpy as np
from PIL import Image

img = Image.open(r'MU.jpg')

img_array = np.array(img)

dimensions = img_array.shape

print("Shape of the image:", dimensions)

print("Image Dimensions (HxW):", img.size[::-1])  

min_blue = img_array[:, :, 2].min()
print("Minimum pixel value at Blue channel:", min_blue)
