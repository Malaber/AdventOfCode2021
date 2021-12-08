import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

occurences = 0


def remove_chars(remove, remove_from):
    for char in list(remove):
        if char in remove_from:
            remove_from = remove_from.replace(char, "")
    return remove_from


for line in lines:
    # decoding[input] = output
    decoding = {}
    decoding_per_digit = {}
    input, output = line.strip().split(" | ")
    output_digits = output.split(" ")
    input_digits = input.split(" ")
    for digit in output_digits:
        unique_digit_amounts = [2, 4, 3, 7]
        if len(digit) in unique_digit_amounts:
            occurences += 1

    input_digits_length = {
                            2: [],
                            3: [],
                            4: [],
                            5: [],
                            6: [],
                            7: [],
                           }
    for digit in input_digits:
        sorted_digit = "".join(sorted(digit))
        input_digits_length[len(digit)].append(sorted_digit)

    while len(decoding.keys()) < 10:
        one = input_digits_length[2][0]
        decoding_per_digit[1] = one
        four = input_digits_length[4][0]
        decoding_per_digit[4] = four
        seven = input_digits_length[3][0]
        decoding_per_digit[7] = seven
        eight = input_digits_length[7][0]
        decoding_per_digit[8] = eight

        decoding[remove_chars(one, seven)] = "a"

        for digit in input_digits_length[6]:
            digit_without_4 = remove_chars(four, digit)
            digit_without_known = remove_chars("".join(decoding.keys()), digit_without_4)
            if len(digit_without_known) == 1:
                # the digit is nine
                decoding[digit_without_known] = "g"
                decoding_per_digit[9] = digit
                break

        for digit in input_digits_length[5]:
            digit_without_4 = remove_chars(four, digit)
            digit_without_known = remove_chars("".join(decoding.keys()), digit_without_4)
            if len(digit_without_known) == 1:
                # the digit is two
                decoding[digit_without_known] = "e"
                decoding_per_digit[2] = digit
                break

        for digit in input_digits_length[5]:
            digit_without_4 = remove_chars(four, digit)
            digit_without_known = remove_chars("".join(decoding.keys()), digit_without_4)
            if len(digit_without_known) == 1:
                # the digit is five
                decoding[digit_without_known] = "e"
                decoding_per_digit[5] = digit
                break

        print()


print("Part 1")
print(occurences)

