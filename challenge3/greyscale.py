from PIL import Image

im = Image.open("pencils.jpg")

width, height = im.size

for y in range(height):
  for x in range(width):
    r, g, b = im.getpixel((x, y))
    grey = int((r + g + b) / 3)
    im.putpixel((x, y), (grey, grey, grey))

im.save("grey.jpg", "JPEG")
