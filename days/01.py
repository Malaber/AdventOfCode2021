import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

depths = [int(depth) for depth in lines]

inc = 0

for i in range(len(depths)):
    this = depths[i]
    last = depths[i-1] if i > 0 else None

    if last:
        if this > last:
            inc += 1

print(inc)
