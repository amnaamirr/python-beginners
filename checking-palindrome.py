"""Write a program to check whether given input is palindrome or not """
# palindrome is a number which reads the same forward or backward
num = (input("ENTER A NUMBER: "))
reverse_num = num[::-1]
while int(num) > 9:
    if num == reverse_num:
        print(f"THE NUMBER {num} IS A PALINDROME!")
        break
    else:
        print(f"THE NUMBER {num} IS NOT A PALINDROME!")
        break
else:
    print(f"THE NUMBER {num} IS NOT A PALINDROME!")
