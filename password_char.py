password=input("emter the password:")
confirm_password=input("enter the password again:")
if not 8<= len(password) <=12:
    print("the password must have 8-12 characters.")
else:
    if password==confirm_password:
        print("password set.")
    else:
        print("the passwrods didnt match.")