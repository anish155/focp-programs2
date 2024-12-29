bad_passwords = ["password", "letmein", "sesame", "hello", "justinbieber"]
password = input("Enter the password: ")
confirm_password = input("Enter the password again: ")

if password in bad_passwords:
    print("The password is too common. Please use a proper format instead of bad passwords.")
elif not (8 <= len(password) <= 12):
    print("The password must have 8-12 characters.")
elif password != confirm_password:
    print("The passwords didn't match.")
else:
    print("Password set successfully.")
