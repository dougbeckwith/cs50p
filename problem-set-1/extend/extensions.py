import os

# Prompt the user to enter the name of a file.
file_name = input("File name: ")

# Extract the file extension from the provided file name and convert it to lowercase.
file_extension = os.path.splitext(file_name)[1].lower().strip()

# Output the media type based on the file extension.
match file_extension:
    case ".gif":
        print("image/gif") 
    case ".jpg" | ".jpeg":
        print("image/jpeg ")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")

