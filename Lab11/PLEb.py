import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r'MU.jpg')
img_array = np.array(img)

top, bottom, left, right = 50, 50, 100, 100

padded_img = np.pad(
    img_array, 
    ((top, bottom), (left, right), (0, 0)),  
    mode='constant', 
    constant_values=0
)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(padded_img)
plt.title("Image with Black Padding")
plt.axis("off")

plt.tight_layout()
plt.show()
