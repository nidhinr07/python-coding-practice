text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if len(text1) == len(text2) and text2 in text1 + text1:
    print("Strings are rotations")
else:
    print("Strings are not rotations")
