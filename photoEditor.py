from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"  # folder for unedited images
pathOut = "/editedImgs"  # folder for edited images


def saving_imgs(filename, edit):
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')


def beautify():
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")

        # sharpening, BW
        edit = img.filter(ImageFilter.SHARPEN)

        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        bright = 1.2
        brightness = ImageEnhance.Brightness(edit)
        enhancer.enhance(factor)
        edit = brightness.enhance(bright)

        saving_imgs(filename, edit)
    print('Images were edited')


def color_convert():
    try:
        factor = float(input('Write color value (in 0.0 form where first number is black, and second white): '))
        for filename in os.listdir(path):
            img = Image.open(f"{path}/{filename}")

        enhancer = ImageEnhance.Color(img)
        edit = enhancer.enhance(factor)

        saving_imgs(filename, edit)
        print('Images were edited')
    except ValueError as e:
        print(e)
        print('You can only write a number in format: 0.0')


def rotate():
    try:
        rotation = int(input('Write rotation (90, 180, -90, -180): '))
        for filename in os.listdir(path):
            img = Image.open(f"{path}/{filename}")

            edit = img.rotate(rotation)

            saving_imgs(filename, edit)
        print('Images were edited')
    except ValueError as e:
        print(e)
        print('You can only write a numbers from (90, 180, -90, -180)')


def sharpness():
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")

        edit = img.filter(ImageFilter.SHARPEN)

        saving_imgs(filename, edit)
    print('Images were edited')


def contrast():
    try:
        factor = float(input('Write contrast value (>=1): '))
        for filename in os.listdir(path):
            img = Image.open(f"{path}/{filename}")

            enhancer = ImageEnhance.Contrast(img)
            edit = enhancer.enhance(factor)

            saving_imgs(filename, edit)
        print('Images were edited')
    except ValueError as e:
        print(e)
        print('You can only write a numbers from 1')


def brightness():
    try:
        factor = float(input('Write brightness value (>=1): '))
        for filename in os.listdir(path):
            img = Image.open(f"{path}/{filename}")

            enhancer = ImageEnhance.Brightness(img)
            edit = enhancer.enhance(factor)

            saving_imgs(filename, edit)
        print('Images were edited')
    except ValueError as e:
        print(e)
        print('You can only write a numbers from 1')


def resize():
    try:
        width = int(input('Write image width: '))
        height = int(input('Write image height: '))
        for filename in os.listdir(path):
            img = Image.open(f"{path}/{filename}")

            edit = img.resize((width, height))

            saving_imgs(filename, edit)
        print('Images were edited')
    except ValueError as e:
        print(e)
        print('You can only write a full numbers as width and height')


# editing pic

while True:
    print('''
    Chose edit mode:
        (1) beautify mode (sharpen, contrast, brightness etc.)
        (2) color convert
        (3) rotate photo
        (4) sharpness
        (5) contrast
        (6) brightness
        (7) resize
        (0) to exit''')
    chosen_option = input('Write a number to choose:')

    if chosen_option == '1':
        beautify()
    elif chosen_option == '2':
        color_convert()
    elif chosen_option == '3':
        rotate()
    elif chosen_option == '4':
        sharpness()
    elif chosen_option == '5':
        contrast()
    elif chosen_option == '6':
        brightness()
    elif chosen_option == '7':
        resize()
    elif chosen_option == '0':
        break
    else:
        print('Write a number from 1 to 7')
