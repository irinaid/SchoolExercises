from PIL import Image

im = Image.open("pencils.jpg")

im.save("new_image.jpg", "JPEG")
