from PIL import Image, ImageFilter, ImageFile
path = 'images/totally_normal_pic.jpg'
img = Image.open(path)

img.show()


with Image.open(path) as img:
    img_gray = img.convert("L")
    edges = img_gray.filter(ImageFilter.FIND_EDGES)
    edges.save('images/totally_normal_pic.png')