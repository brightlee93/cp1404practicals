MIN_LENGTH = 10


def main():
    password = get_password()
    while password < MIN_LENGTH:
        print("password not long enough")
        password = get_password()
    print_password(password)


def print_password(password):
    # print result with asterik
    print(len(password) * "*")


def get_password():
    # get password input
    password = input("Enter Password: ")
    return password


main()