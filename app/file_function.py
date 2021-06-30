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
                return "Your text has been added"

        except FileNotFoundError as errmsg:
            return f"File not found: {errmsg}."
