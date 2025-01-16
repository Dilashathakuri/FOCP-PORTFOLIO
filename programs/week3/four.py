BAD_PASSWORDS = ['password', 'letmein', 'hello', 'password','asdfghjkl','abcdefg','1234567']

password1 = input("Enter a new password (8-12 characters): ")
password2 = input("Confirm the password: ")

if password1 == password2 and 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
    print("Password Set!")
else:
    print("Error: Invalid password.")
