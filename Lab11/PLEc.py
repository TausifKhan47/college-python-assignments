import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r'MU.jpg')
img_array = np.array(img)

R = img_array[:, :, 0]   
G = img_array[:, :, 1]   
B = img_array[:, :, 2]   

plt.figure(figsize=(12, 6))

plt.subplot(1, 4, 1)
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(R, cmap="Reds")
plt.title("Red Channel")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(G, cmap="Greens")
plt.title("Green Channel")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(B, cmap="Blues")
plt.title("Blue Channel")
plt.axis("off")

plt.tight_layout()
plt.show()
