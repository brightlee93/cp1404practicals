import os
import shutil


def main():
    os.chdir("FilesToSort")

    for file in os.listdir('.'):
        extension = file.split(".")[1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print(file, extension)
        shutil.move(file, extension+"/" + file)



main()
