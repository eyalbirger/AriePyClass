from PIL import Image, ImageFilter, ImageFile
from pathlib import Path
import numpy as np
import os



pth = 'images/totally_normal_pic.jpg'
newPth = Path("images/totally_normal_pic.png")
img = Image.open(pth)

#with vectors
arr = np.array(img)
red = np.sum(arr[:, :, 0])
green = np.sum(arr[:, :, 1])
blue = np.sum(arr[:, :, 2])

print(f"red: {red}, green: {green}, blue: {blue}")