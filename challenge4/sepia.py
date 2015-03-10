from PIL import Image

im = Image.open("pencils.jpg")
width, height = im.size

for y in range(height):
  for x in range(width):
    r, g, b = im.getpixel((x, y))
    newR = (r * .393) + (g *.769) + (b * .189)
    newG = (r * .349) + (g *.686) + (b * .168)
    newB = (r * .272) + (g *.534) + (b * .131)
    im.putpixel((x, y), (int(newR), int(newG), int(newB)))

im.save("sepia.jpg", "JPEG")

