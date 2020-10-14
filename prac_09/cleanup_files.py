"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os
import re


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        for count, character in enumerate(filename):
            try:
                if filename[count].islower() and filename[count + 1].isupper():
                    filename = filename[:count + 1] + "_" + filename[count + 1:]
                if filename[count].isdigit() and filename[count+1].isalpha():
                    filename = filename[:count + 1] + "_" + filename[count + 1:]
            except IndexError:
                pass

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.title().replace(" ", "_").replace(".Txt", ".txt")
    return new_name


main()
