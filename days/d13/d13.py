import re
from sympy import symbols, Eq, solve

_input = open("input.txt").read().split("\n\n")
games = []
for section in _input:
    nums = list(map(int, re.findall(r"(\d+)", section)))
    games.append(((nums[0], nums[1]), (nums[2], nums[3]), (nums[4], nums[5])))



def solve_two_linear_equations(coefficients, constants):
    x, y = symbols('x y')
    a, b = coefficients[0]
    d, e = coefficients[1]
    c, f = constants
    eq1 = Eq(a * x + b * y, c)
    eq2 = Eq(d * x + e * y, f)
    solution = solve((eq1, eq2), (x, y))

    if solution:
        return solution[x], solution[y]

def calculate_price(b=False):
    tokens = 0
    for game in games:
        A, B, price = game
        if b:
            price = (price[0] + 10000000000000, price[1] + 10000000000000)
        num_A, num_B = solve_two_linear_equations([(A[0], B[0]), (A[1], B[1])], [price[0], price[1]])
        if num_A.is_integer and num_B.is_integer:
            tokens += num_A * 3 + num_B
    return tokens

print(f"Part 1: {calculate_price()}", f"Part 2: {calculate_price(True)}", sep="\n")
