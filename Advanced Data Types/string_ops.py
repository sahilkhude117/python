text = input("Enter a string: ")

vowels = consonants = spaces = digits = special_chars = 0

vowel_set = 'aeiouAEIOU'

for char in text:
    if char in vowel_set:
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_chars += 1


print("\nAnalysis of the given string:")
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Blank Spaces:", spaces)
print("Special Characters:", special_chars)