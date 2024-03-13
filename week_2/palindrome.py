#This is a program that reverses the order of characters in a string and detects palindromes.
#Date: 22.02.2024
#Name: Simon Munene

character=str(input("Enter the desired word:"))
new_character=character[::-1]
print(new_character)

if (new_character == str(character)):
    print("The word is a palindrome.")
else:
    print("The word is not a palindome.")