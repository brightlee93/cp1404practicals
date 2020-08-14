# OUTFILE = "name.txt"
# out_file = open(OUTFILE, "w")
# name = input("What is your name? ")
# out_file.write(name)
# out_file.close()
#
# INFILE = "name.txt"
# in_file = open(INFILE, "r")
# read_name = in_file.read()
# print("Your name is {}".format(read_name))
# in_file.close()
#
# in_number_file = open("numbers.txt", "r")
# numbers = in_number_file.readlines()
# number1 = int(numbers[0])
# number2 = int(numbers[1])
# total = number1 + number2
# print(total)
# in_number_file.close()

in_number_file = open("numbers.txt", "r")
numbers = in_number_file.readlines()
total = 0
for i in numbers:
    number = int(i)
    total += number
print(total)
in_number_file.close()

