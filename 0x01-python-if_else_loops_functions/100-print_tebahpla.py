#!/usr/bin/python3

output = ""
for char in range(122, 96, -1):
    if char % 2 == 0:
        output += "{:c}".format(char)
    else:
        output += "{:c}".format(char - 32)

print(output, end="")
