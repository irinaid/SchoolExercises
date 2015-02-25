# PIL is the Python library for image processing
# The Image module helps process images
from PIL import Image
# os is the Python library that interacts with the
# operating system
from os import mkdir

# Open an image and save it in a variable
tulips = Image.open('winxptulip.jpg')

# Rotate an image
rotated_tulips = tulips.rotate(45)
rotated_tulips.save("rotated45", "JPEG")

# Rotate the image upside down
upside_down = tulips.rotate(90).rotate(90).rotate(90)
upside_down.save("upside_down", "JPEG")

# Exercise: rotate the image using a for loop


# Exercise: what happens if you rotate 45 degrees?
# What about the corners? 


# Flip an image from left to right (mirror it)
pencils = Image.open('pencils.jpg')
flipped = pencils.transpose(Image.FLIP_LEFT_RIGHT)
flipped.save("flipped", "JPEG")

# Flip an image top to bottom
flipped_up = pencils.transpose(Image.FLIP_TOP_BOTTOM)
flipped_up.save("flipped_up", "JPEG")

bliss = Image.open('winxpbliss.jpg')
bird = Image.open('bird.jpg')

photos_album = [tulips, pencils, bliss, bird]

# Make a new directory
mkdir("album")

# Iterate over the album and change all photos at once
for i in range(0, len(photos_album)):
  image = photos_album[i].rotate(45)
  image.save("album/image" + str(i), "JPEG")

# Iterate over the list to make other transformations!
for i in range(0, len(photos_album)):
  image = photos_album[i].rotate(180)
  image.save("album/rotated_image" + str(i), "JPEG")
  
for i in range(0, len(photos_album)):
  image = photos_album[i].transpose(Image.FLIP_LEFT_RIGHT)
  image.save("album/flipped_image" + str(i), "JPEG")
  
