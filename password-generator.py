# random-password-generator
import random
username = input("USERNAME: ")
# asking the user for the length of the password.
print("HOW MANY CHARACTERS SHOULD THE PASSWORD HAVE?\n  MINIMUM CHARACTERS = 8\n  MAXIMUM CHARACTERS = 12")
length_password = int(input("NO. OF CHARACTERS IN PASSWORD: "))

while length_password >= 8 and length_password <= 12:

    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_char = ["@", "#", "$", "%", "&", "*", "!"]
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                   "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # choosing a charactor randomly from each list
    num_char = random.choice(digits)
    sp_char = random.choice(special_char)
    alpha_l = random.choice(alpha_lower)
    alpha_u = random.choice(alpha_upper)
    # filling the rest of the length of password using lowercase letters
    length = length_password - 4
    alpha = ""
    for i in range(length):
        alpha = alpha+(random.choice(alpha_lower))
    # joining the characters to make password
    passwordlist = [num_char, sp_char, alpha_l, alpha_u, alpha]
    random.shuffle(passwordlist)
    password = "".join(passwordlist)
    print(f'PASSWORD: {password}')
    exit()

else:
    print("oops!\nTHE LENGTH OF PASSWORD SHOULD BE WITHIN 8-12")
