import numpy as np
from PIL import Image
from colorama import Fore, init

init(autoreset=True)

def ascii_convert(image_path, width):
    img = Image.open(image_path)
    img = img.convert('L')
    aspect_ratio = img.height / img.width
    new_width = width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_img = img.resize((new_width, new_height))
    pixels = np.array(resized_img)

    ascii_str = ''
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
    for row in pixels:
        for pixel_value in row:
            ascii_str += ascii_chars[pixel_value // 25]
        ascii_str += '\n'

    return ascii_str

# Input width and image file path
width = int(input("Enter the width of the ASCII art: "))
image_path = input("Enter the image file path: ")

# Convert the image to ASCII art
result_ascii = ascii_convert(image_path, width)

# Output the result
print(Fore.GREEN + result_ascii)

# Ask if the user wants to save the ASCII art to a text file
save_choice = input("Do you want to save the ASCII art to a text file? (y/n): ")
if save_choice.lower() == 'y':
    file_path = "OutPut-ASCII_art.txt"
    try:
        with open(file_path, 'a') as f:
            f.write("\n" + result_ascii)
        print(f"ASCII art appended to {file_path}")
    except FileNotFoundError:
        with open(file_path, 'w') as f:
            f.write(result_ascii)
        print(f"ASCII art saved to {file_path}")
elif save_choice.lower() == 'n':
    print("Exiting...")
else:
    print("Invalid input. Exiting...")
