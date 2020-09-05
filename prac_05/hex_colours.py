NAME_TO_HEX_CODE = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4", "azure": "#f0ffff",
                    "beige": "#f5f5dc", "bisque": "#ffe4c4", "black": "#000000", "blue": "#0000ff",
                    "blanchedalmond": "#ffebcd", "blueviolet": "#8a2be2"}

name = input("Colour name: ").lower()
while name != "":
    if name in NAME_TO_HEX_CODE:
        print("{0} is {1}".format(name, NAME_TO_HEX_CODE[name]))
    else:
        print("incorrect input")
    name = input("Colour name: ").lower()
