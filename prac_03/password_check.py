MIN_LENGTH = 10
password = input("Enter Password: ")
if len(password) >= MIN_LENGTH:
    print(len(password) * "*")
else:
    print("password not long enough")
