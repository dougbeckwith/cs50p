# Figlet Text Generator

## Description

The **Figlet Text Generator** is a Python program that uses the PyFiglet library to create stylized text from user input. It provides options for customizing the font used to render the text, making it a fun tool for creating text art.

## Usage

1. **Clone or Download the Repository:**

   To use the Figlet Text Generator, you need to clone or download the repository to your local machine. You can do this by clicking on the "Code" button and selecting your preferred method.

2. **Navigate to the Directory:**

   Open a terminal or command prompt and navigate to the directory where you saved the Python script (`figlet.py`) using the `cd` command.

3. **Install Dependencies:**

   ```bash
   pip install pyfiglet
   ```

4. **Run the Program:**

   Execute the following command to run the program:

   ```bash
   python figlet.py
   ```

5. **Customize Fonts (Optional):**

   You can specify a font using the `-f` or `--font` command-line argument, followed by the font name. For example:

   ```bash
   python figlet.py -f slant
   ```

   This sets the font to "slant." If you don't specify a font, a random font will be selected.

6. **Input and Output:**

   The program will prompt you to enter text. After you've entered your text, it will render and display the stylized output using the selected or random font.

## Example

Here's a simple example of how to use the Figlet Text Generator:

```plaintext
$ python figlet.py -f slant
Input: CS50
Output:
   ___________ __________
  / ____/ ___// ____/ __ \
 / /    \__ \/___ \/ / / /
/ /___ ___/ /___/ / /_/ /
\____//____/_____/\____/
```

Enjoy creating stylish text art! 😊
