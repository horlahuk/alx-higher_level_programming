#!/usr/bin/python3

for c in range(97, 123):
    if c == q or c == e:
        continue
    print("{:c}".format(c), end="")
