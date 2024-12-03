import re
import math
text = open("input.txt").read()
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
matches = re.findall(pattern, text)
remove, dont = [], False
for i, match in enumerate(matches):
    if match == "don't()":
        dont = True
    elif match == "do()":
        dont = False
    elif dont:
        remove.append(i)
p1 = sum([math.prod(map(int, match[4:-1].split(","))) for match in matches if "do" not in match])
p2 = sum([math.prod(map(int, match[4:-1].split(","))) for i, match in enumerate(matches) if i not in remove and "do" not in match])
print(f"Part 1: {p1}\nPart 2: {p2}")
