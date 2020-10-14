import os
import shutil


def main():
    os.chdir("FilesToSort")
    extension_to_category = {}
    for file in os.listdir('.'):
        extension = file.split(".")[1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} file into? ".format(extension))
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        shutil.move(file, extension_to_category[extension] + "/" + file)


main()
