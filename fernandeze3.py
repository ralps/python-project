# author : Maurice Ralph Fernandez

import sys

data = input("Enter a comma separated list of numbers:")

total = sum([float(k)**2 for k in data.split(",")])
numbers = data.split(",")
total = 0.0
for i in numbers:
    g = float (f)
    total += g ** 2

print("sum of squares:{:.2f}".format(total))




