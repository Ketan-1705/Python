#Write a Python program to count how many times each character appears in a string.


string = "hello world"
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character occurrences:")
for key, value in char_count.items():
    print(f"{key} : {value}")
