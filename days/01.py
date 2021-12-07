import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

depths = [int(depth) for depth in lines]

def count_increases(depths):
    inc = 0
    for i in range(len(depths)):
        this = depths[i]
        last = depths[i - 1] if i > 0 else None

        if last:
            if this > last:
                inc += 1
    return inc


print("Part 1")
print(count_increases(depths))


print("Part 2")

windows = []
for i in range(len(depths)):
    # print(i)
    a, b, c = 0, 0, 0
    try:
        a = depths[i]
        b = depths[i+1]
        c = depths[i+2]
    except IndexError as e:
        continue

    windows.append(a+b+c)

print(count_increases(windows))
