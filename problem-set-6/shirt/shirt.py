import sys
import os
from PIL import Image
from PIL import ImageOps


def main():
    # Check if the command line arguments are correct
    check_argv_length()
    check_input_file_exists()
    check_file_extensions()


    shirt_image = open_image("shirt.png")
    input_image = open_image(sys.argv[1])

    # Process the input image and add the shirt image
    input_image_edit = process_image(input_image, shirt_image)

    # Save the resulting image to the user-specified output file
    save_image(input_image_edit, sys.argv[2])


def open_image(file):
    try:
        return Image.open(file)
    except FileNotFoundError:
        sys.exit("File Not Found")


def save_image(image, output_file):
    try:
        image.save(output_file)
    except ValueError:
        sys.exit("Output format could not be determined from the file name")
    except OSError:
        sys.exit("File could not be written")


def process_image(input_image, shirt_image):
    try:
        input_image_edit = ImageOps.fit(input_image, [600, 600])
        input_image_edit.paste(shirt_image, shirt_image)
        return input_image_edit
    except Exception as e:
        sys.exit(f"Image processing error: {e}")


def check_argv_length():
    arg_length = len(sys.argv)
    if arg_length < 3:
        sys.exit("Too few command-line arguments")
    if arg_length > 3:
        sys.exit("Too many command-line arguments")


def check_input_file_exists():
    if not os.path.exists(sys.argv[1]):
        sys.exit("Input does not exist")


def check_file_extensions():
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_file_extension = os.path.splitext(sys.argv[1])[1].lower()
    output_file_extension = os.path.splitext(sys.argv[2])[1].lower()

    if input_file_extension != output_file_extension:
        sys.exit("Input and output have different extensions")

    if not input_file_extension in valid_extensions:
        sys.exit("Invalid output")

    if not output_file_extension in valid_extensions:
        sys.exit("Invalid output")


if __name__ == "__main__":
    main()
