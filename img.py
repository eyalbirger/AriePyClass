from PIL import Image, ImageFilter, ImageFile
from pathlib import Path
import os



pth = 'images/totally_normal_pic.jpg'
newPth = Path("images/totally_normal_pic.png")
img = Image.open(pth)

img.show()


with Image.open(pth) as img:
    img_gray = img.convert("L")
    edges = img_gray.filter(ImageFilter.FIND_EDGES)
    edges.save('images/totally_normal_pic.png')
    
    if newPth.is_file():
        print("exists but now im deleting this shit")
        os.remove(newPth)