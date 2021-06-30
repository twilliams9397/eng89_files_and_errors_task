from app.file_function import FileOpen

while True:
    filename = input("What is the name of the .txt file you would like to open?  ")
    print(FileOpen.find_txt(filename))
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
