from Source import rpg

marks = True
password_length = input("Enter the length of password : ")

if "F" in password_length:
    marks = False
    password_length = password_length.replace("F", "")

password = rpg.generate_password(password_length, marks)
rpg.creator()
print("Your password is: ", password)
