email_to_name = {}
email = input("Email: ")
while email != "":
    name, domain = email.split("@")
    if "." in name:
        first_name, last_name = name.split(".")
        name = first_name + " " + last_name
    name_check = input("Is your name {0}? (Y/n) ".format(name.title())).lower()
    while name_check == "y" or name_check == "yes" or name_check == "":
        email_to_name[name.title()] = email
        name_check = 0
        email = input("Email: ")
    while name_check == "n" or name_check == "no":
        name = input("Name: ")
        email_to_name[name.title()] = email
        name_check = 0
        email = input("Email: ")
for name, email in email_to_name.items():
    print("{0} ({1})".format(name, email))



# for name in email_to_name:
#     print("{0} ({1})".format(name, email_to_name[name]))


