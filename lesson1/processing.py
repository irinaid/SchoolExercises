# PIL is the Python library for image processing
# The Image module helps process images
from PIL import Image
# os is the Python library that interacts with the
# operating system
import os
# High level file operations in Python
import shutil

# Open an image and save it in a variable
p = Image.open('pencils.jpg')
width, height = p.size
#r,g,b = p.getpixel((0,0))
#p.putpixel((0,0), (r,g,b))

# grayscale
for i in range(width):
  for j in range(height):
    r, g, b = p.getpixel((i,j))
    gray = (r + g + b) / 3
    p.putpixel((i, j), (gray, gray, gray))

p.save("gray.jpg", "JPEG")

# open the image again
p = Image.open('pencils.jpg')
# uncomment if opening a different phone
# width, height = p.size

# sepia tone

for i in range(width):
  for j in range(height):
    inputRed, inputGreen, inputBlue = p.getpixel((i,j))
    outputRed = (inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)
    outputGreen = (inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)
    outputBlue = (inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)
    p.putpixel((i,j), (int(outputRed), int(outputGreen), int(outputBlue)))

p.save("sepia.jpg", "JPEG")

