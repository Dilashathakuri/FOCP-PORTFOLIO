password1 = input("Enter a new password: ")
password2 = input("Confirm the password: ")

if password1 == password2:
    print("Password Set!")
else:
    print("Error: Passwords do not match.")
