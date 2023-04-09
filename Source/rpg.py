import string
import random


def generate_password(length, marks=True):
    try:

        length = int(length)
        letters = string.ascii_letters
        digits = string.digits
        punctuation = string.punctuation

        if not (marks):
            punctuation = ""

        all_chars = letters + digits + punctuation
        password = "".join(random.sample(all_chars, length))

        return password

    except ValueError:
        print("This program has the ability to create passwords with a length of 8 to 94 characters.")
        raise


def creator():
    contact = ("""
#############################################################
#          PYTHON - Random Password Generetor (RPG)         #
#############################################################
#                         CONTACT                           #
#############################################################
#      DEVELOPER :                 Aliht                    #
#      Mail Address :     aliht.workspace@gmail.com         #
#      LINKEDIN :   https://www.linkedin.com/in/al-iht      #
#############################################################
	""")
    print(contact)
