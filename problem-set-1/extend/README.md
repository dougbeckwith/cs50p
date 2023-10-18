# File Media Type Detector

The File Media Type Detector is a Python program that allows you to determine the media type of a file based on its file extension. It prompts the user to enter the name of a file, extracts the file extension, and then provides the corresponding media type for that file extension.

## Usage

1. Run the program by executing it with a Python interpreter.

   ```bash
   python extension.py
   ```

2. Enter the name of the file for which you want to determine the media type.

3. The program will output the media type based on the file extension.

## Input

The program expects the user to provide the name of the file for which they want to determine the media type.

## Output

The program extracts the file extension from the provided file name, converts it to lowercase, and outputs the corresponding media type for the file extension. If the file extension is not recognized, it defaults to "application/octet-stream."

## Supported Media Types

The program recognizes the following media types and their corresponding file extensions:

- `image/gif` for ".gif" files.
- `image/jpeg` for ".jpg" and ".jpeg" files.
- `image/png` for ".png" files.
- `application/pdf` for ".pdf" files.
- `text/plain` for ".txt" files.
- `application/zip` for ".zip" files.
