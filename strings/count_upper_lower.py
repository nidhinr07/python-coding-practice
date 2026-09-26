text = input("Enter a string: ")

upper = 0
lower = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Uppercase characters:", upper)
print("Lowercase characters:", lower)
