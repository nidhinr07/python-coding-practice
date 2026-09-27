text = input("Enter a string: ")

for char in text:
    if text.count(char) == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found")
