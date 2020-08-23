# numbers = []
# for i in range(1, 6, 1):
#     number = int(input("Number {}:".format(i)))
#     numbers.append(number)
# first_number = numbers[0]
# last_number = numbers[-1]
# min_number = min(numbers)
# max_number = max(numbers)
# average_number = sum(numbers) / len(numbers)
# print("The first numbers is {}".format(first_number))
# print("The last numbers is {}".format(last_number))
# print("The smallest numbers is {}".format(min_number))
# print("The largest numbers is {}".format(max_number))
# print("The average of the numbers is {}".format(average_number))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_input = input("Your username: ")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
