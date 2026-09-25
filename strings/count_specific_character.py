text = input("Enter a string: ")
char = input("Enter a character to count: ")

count = text.lower().count(char.lower())

print("Character count:", count)
