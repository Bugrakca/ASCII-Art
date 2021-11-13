from PIL import Image
# Open an image as image object
with Image.open("images/ascii-pineapple.jpg") as im:
    # Print the image metadata
    print(im.format, im.size, im.mode)
    print(f"Image size: {im.size}")
# Get width and height of image
width, height = im.size
