import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

print("Part 1")
occurences = 0
for line in lines:
    input, output = line.split(" | ")
    output_digits = output.strip().split(" ")
    for digit in output_digits:
        unique_digit_amounts = [2, 4, 3, 7]
        if len(digit) in unique_digit_amounts:
            occurences += 1

print(occurences)
