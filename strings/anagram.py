text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if sorted(text1.lower()) == sorted(text2.lower()):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
