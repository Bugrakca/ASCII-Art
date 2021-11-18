from PIL import Image
from colorama import Fore

# Get the file path
file_path = "images/ww.jpg"

# Define the ASCII characters and Max Pixel Value
ASCII_CHARS = ' .,:°*oO&$'
MAX_PIXEL_VALUE = 256


# Open an image as image object
image = Image.open(file_path)
image.thumbnail((600, 200)) # Resize the image to a smaller size

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

#* Convert RGB pixel data to Brightness value with different algorithms
def rgb_to_brightness(algo = "avarage", ):
    '''Converting RGB pixel data to brightness values'''
    list_of_brightness = list()
    temporary_list = list()
    for in_list in get_pixel_data():
        for tuple in in_list:
            if algo == "avarage": # Avarage Algorithm
                tuple = round((tuple[0]+tuple[1]+tuple[2]) // 3)
            elif algo == "luminosity": # luminosity Algorithm
                tuple = round((0.21 * tuple[0]) + (0.72 * tuple[1]) + (0.07 * tuple[2]))
            elif algo == "lightness": # Lightness Algorithm
                tuple = round((max(tuple[0], tuple[1], tuple[2]) + min(tuple[0], tuple[1], tuple[2])) / 2)
            else: # Raise an error if the algo is not recognized
                raise Exception(f"Unrecognized algo_name: {algo}")
            temporary_list.append(tuple)
    # Adding the tuples to the list, creating a 2d array.
    for i in range(0, len(temporary_list), image.width):
        list_of_brightness.append(temporary_list[i:i+image.width])
    return list_of_brightness

def invert_brightness(brightness_values = rgb_to_brightness()):
    '''Inverting the brightness values'''
    inverted_brightness_values = list()
    for inverted in brightness_values:
        inverted_brightness_values.append([MAX_PIXEL_VALUE - x for x in inverted])
    return inverted_brightness_values

def create_ascii_art(color = Fore.WHITE):
    '''Turning brightness values into an ASCII strings. An print it out.'''
    for br in invert_brightness():
        for x in br:
            x = ((x * len(ASCII_CHARS) // MAX_PIXEL_VALUE)) # I divide 256 because the pixel values is 0-255 with zero included. That is give me a 256.
            ascii_val = ASCII_CHARS[x]
            print(color + ascii_val, end='  ') # I added two spaces between the characters so that the image doesn't look squashed.
        # Printing new line is necessary for this method. Otherwise, the image
        # doesn't look like as expected.
        print("\n")


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
#     for pixels in rgb_to_brightness():
#         for pixel in pixels:
#             put_pixel_data.append(pixel)
#     im.putdata(put_pixel_data)
#     im.show()

get_pixel_data()
# rgb_to_brightness(algo = "luminosity")
invert_brightness(rgb_to_brightness(algo = "luminosity"))
create_ascii_art()
# get_pixel_data_2()
# put_pixels()
