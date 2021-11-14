from PIL import Image, ImageDraw


file_path = "images/ascii-pineapple.jpg"

# Open an image as image object
image = Image.open(file_path)

# Print the image metadata
print(image.format, image.size, image.mode)
print(f"Image size: {image.size}")

#* Get pixel data (First Method)
def get_pixel_data():
    '''Getting a pixel data from getdata() method.
    Get data method has to be turned into an array.'''
    all_pixels = list()
    pixels = list(image.getdata())
    # List comprehension
    # all_pixels = [pixels[i:i+image.width] for i in range(0, len(pixels), image.width)]
    for x in range(0, len(pixels), image.width):
        all_pixels.append(pixels[x:x+image.width])
    return all_pixels

#* Get pixel data (Second Method)
def get_pixel_data_2():
    '''Getting a pixel data from load() method.'''
    pixel_data = list()
    image_data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel_data.append(image_data[x,y])
    return pixel_data

#* Create an image with a list of pixel data
def put_pixels():
    '''Puts the pixel data into a putdata() method and create an image with RGB
    pixel data. Then display the image with OS default application.'''
    put_pixel_data = list()
    im = Image.new("RGB", (image.width, image.height))
    for pixels in get_pixel_data_2():
        for pixel in pixels:
            put_pixel_data.append(pixel)
    im.putdata(get_pixel_data_2())
    im.show()

get_pixel_data_2()
put_pixels()
