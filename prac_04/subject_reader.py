"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    format_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data_list.append(parts)
        print("----------")
    input_file.close()
    return data_list


def format_data(data):
    for i in data:
        subject = i[0]
        lecturer = i[1]
        number_of_student = i[2]
        print("{} is taught by {:10} and has {:3} students".format(subject, lecturer, number_of_student))


main()