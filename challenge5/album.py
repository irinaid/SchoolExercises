from PIL import Image

# os is the Python library that interacts with the
# operating system
import os

# Open an image and save it in a variable
tulips = Image.open("tulips.jpg")
pencils = Image.open("pencils.jpg")
winxp = Image.open("winxp.jpg")
bird = Image.open("bird.jpg")

photos_album = [tulips, pencils, winxp, bird]
photos_names = ["tulips", "pencils", "winxp", "bird"]

# Make a new directory
os.mkdir("album")

# Iterate over the album and change all photos at once
for i in range(0, len(photos_album)):
  im = photos_album[i]
  rotated = im.rotate(45)
  rotated_name = "album/" + photos_names[i] + "_rotated.jpg"
  rotated.save(rotated_name, "JPEG")
