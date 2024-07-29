import random
import string

def password(min_len, num=True, special_char=True):
    letter = string.ascii_letters
    digit = string.digits
    special = string.punctuation

    character = letter
    if num:
        character += digit
    if special_char:
        character += special

    pwd = ""
    has_num = not num
    has_special = not special_char

    while len(pwd) < min_len or not (has_num and has_special):
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digit:
            has_num = True
        elif new_char in special:
            has_special = True

    return pwd

min_len = int(input("Enter the length of the password: "))
has_num = input("Do you want to have numbers? (y/n): ").lower() == "y"
has_special = input("Do you want to have special characters? (y/n): ").lower() == "y"

pwd = password(min_len, has_num, has_special)
print("The generated password is:", pwd)
