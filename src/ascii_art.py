from PIL import Image


file_path = "images/ww.jpg"

ASCII_CHARS = '`.,:irs?@9B&#$'


# Open an image as image object
image = Image.open(file_path)
image.thumbnail((600, 200))

# Print the image information
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

#* Convert RGB pixel data to Brightness value
def rgb_to_brightness():
    '''Converting RGB pixel data to brightness values'''
    list_of_brightness = list()
    temporay_list = list()
    for in_list in get_pixel_data():
        for tuple in in_list:
            tuple = (tuple[0]+tuple[1]+tuple[2]) // 3
            temporay_list.append(tuple)
    for i in range(0, len(temporay_list), image.width):
        list_of_brightness.append(temporay_list[i:i+image.width])
    return list_of_brightness


#* Get pixel data (Second Method)
# def get_pixel_data_2():
#     '''Getting a pixel data from load() method.'''
#     pixel_data = list()
#     image_data = image.load()
#     for y in range(image.height):
#         for x in range(image.width):
#             pixel_data.append(image_data[x,y])
#     return pixel_data

#* Create an image with a list of pixel data
# def put_pixels():
#     '''Puts the pixel data into a putdata() method and create an image with RGB
#     pixel data. Then display the image with OS default application.'''
#     put_pixel_data = list()
#     im = Image.new("RGB", (image.width, image.height))
#     for pixels in get_pixel_data_2():
#         for pixel in pixels:
#             put_pixel_data.append(pixel)
#     im.putdata(get_pixel_data_2())
#     im.show()

get_pixel_data()
rgb_to_brightness()
# get_pixel_data_2()
# put_pixels()
