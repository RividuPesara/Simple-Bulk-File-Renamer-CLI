import os

def rename():
    directory = input("Enter the directory path: ")
    ending = input("Enter the file extension (e.g., 'txt'): ")
    newname = input("Enter the new name: ")
    
    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return

    files = os.listdir(directory)
    counter = 1
    for file in files:
        if file.endswith(ending):
            filetype = file.split('.')[-1]
            os.rename(os.path.join(directory, file), os.path.join(directory, newname + str(counter) + "." + filetype))
            print("Renaming " + file + " to " + newname + str(counter) + "." + filetype)
            counter += 1

rename()
