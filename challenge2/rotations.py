from PIL import Image

im = Image.open("pencils.jpg")

rotated_image = im.rotate(90)
rotated_image.save("rotated90.jpg", "JPEG")

rotated_image = im.rotate(45)
rotated_image.save("rotated45.jpg", "JPEG")

rotated_image = im.rotate(180)
rotated_image.save("rotated180.jpg", "JPEG")
