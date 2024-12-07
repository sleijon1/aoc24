from itertools import product
import operator
lines = open("input.txt").read().splitlines()
test_values = []
for line in lines:
    test, values = line.split(": ")
    test, values = int(test), list(map(int, values.split(" ")))
    test_values.append((test, values))

def santa_operator(a, b):
    return int(str(a) + str(b))

symbols = {"*": operator.mul, "+": operator.add, }

def find_correct(symbols):
    results = 0
    for test, values in test_values:
        operations = list(product(symbols.keys(), repeat=len(values)-1))
        for combination in operations:
            value = values[0]
            for i, operation in enumerate(combination):
                value = symbols[operation](value, values[i+1])
            if value == test:
                results += test
                break
    return results
p1, p2 = find_correct(symbols), find_correct({**symbols, "||": santa_operator})
print(f"Part 1: {p1}\nPart 2: {p2}")