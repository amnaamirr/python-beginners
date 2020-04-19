""" Write a Python program that accepts a string and calculate the number of digits and letters Sample Data : Python 3.2, Expected Output : Letters 6, Digits 2"""
string = input("ENTER A STRING: ")
number = ['0','1','2','3','4','5','6','7','8','9']
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter = 0
digit = 0
for char in string:
    if char in alphabets:
        letter += 1
    elif char in number:
        digit += 1

print(f'THE NUMBER OF LETTERS IN YOUR STRING IS: {letter}')
print(f'THE NUMBER OF DIGITS IN YOUR STRING IS: {digit}')