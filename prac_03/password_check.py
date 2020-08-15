MIN_LENGTH = 10

def main():
    password = get_password()
    if len(password) >= MIN_LENGTH:
        print_password(password)
    else:
        print("password not long enough")


def print_password(password):
    print(len(password) * "*")


def get_password():
    password = input("Enter Password: ")
    return password


main()