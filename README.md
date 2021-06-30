# Task for files and errors

- create a function to open a file and raise an error if the file does not exist
- place this function within a class and add other functions
- import this package into a separate .py file and execute the functions

### Setup File
```python
from setuptools import setup

# add some information about package
setup(name="Error Check App") # this is required, lines below are optional
version = "1.0"
description = "Python app"
author = "Tom at Sparta Global"
author_email = "twilliams@spartaglobal.com"
url = "http://spartaglobal.com"
```
### Program Function File
```python
class FileOpen:

    def find_txt(filename):
        try:
            open(f"{filename}.txt")
            return "File found."

        except FileNotFoundError as errmsg:
            return f"File not found: {errmsg}."

    def open_txt(filename):

        try:
            with open(f"{filename}.txt", "r") as file:
                return file.read()

        except FileNotFoundError as errmsg:
            return f"File not found: {errmsg}."

    def write_txt(filename, file_text):
        try:
            with open(f"{filename}.txt", "a") as file:
                file.write("\n" + file_text)
                file.close()
                return "Your text has been added"

        except FileNotFoundError as errmsg:
            return f"File not found: {errmsg}."
```
### Program Run File
```python
from app.file_function import FileOpen

while True:
    try:
        filename = input("What is the name of the .txt file you would like to open?  ")
        open(filename + ".txt")
        file = print(FileOpen.find_txt(filename))
        view = input("Would you like to see your file? y/n  ").lower()
        if view == "y":
            print(FileOpen.open_txt(filename))
            write = input("Would you like to add to your file? y/n  ").lower()
            if write == "y":
                file_text = str(input("What text would you like to add? Press enter to complete.  \n"))
                print(FileOpen.write_txt(filename, file_text))
                view_update = input("Would you like to view your file again? y/n  ").lower()
                if view_update == "y":
                    print(FileOpen.open_txt(filename))
                    break
                elif view_update == "n":
                    print("Thank you for visiting, see you again!")
                    break
            elif write == "n":
                print("Thank you for visiting, see you again!")
                break
        elif view == "n":
            write = input("Would you like to add to your file? y/n  ").lower()
            if write == "y":
                file_text = str(input("What text would you like to add? Press enter to complete.  \n"))
                print(FileOpen.write_txt(filename, file_text))
                break
            elif write == "n":
                print("Thank you for visiting, see you again!")
                break
            else:
                print("Thank you for visiting, see you again!")
                break
        else:
            print("Invalid input, please try again.")
    except FileNotFoundError as errmsg:
        print(f"{errmsg}: File not found, please try again.")

```