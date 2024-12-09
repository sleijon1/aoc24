import numpy as np
from collections import defaultdict
from itertools import combinations
lines = list(map(list, (characters := open("input.txt").read()).splitlines()))

"""diagonal is interpreted as any line that can pass through the pairs
of nodes - not only the main diagonal that passes through distinct x and y
diagonals that pass through non-distinct x and y are also counted"""

x_bound, y_bound = len(lines[0]), len(lines)
ntypes = set(characters) - set((".", "\n"))
def get_antinodes(lines, p1):
    antinodes = set()
    node_positions = defaultdict(list)
    for y, row in enumerate(lines):
        for x, node in enumerate(row):
            if node in ntypes:
                node_positions[node].append((x, y))
    for k, v in node_positions.items():
        for pair in combinations(v, 2):
            if not p1:
                antinodes.add(pair[0])
                antinodes.add(pair[1])
            x_diff, y_diff = abs(pair[0][0] - pair[1][0]), abs(pair[0][1] - pair[1][1])
            i = 1
            while True:
                node_one_out_of_bounds, node_two_out_of_bounds = False, False
                if pair[0][0] <= pair[1][0]:
                    antinode_one_x = pair[0][0] - i*x_diff
                    antinode_two_x = pair[1][0] + i*x_diff
                else:
                    antinode_one_x = pair[0][0] + i*x_diff
                    antinode_two_x = pair[1][0] - i*x_diff
                if pair[0][1] <= pair[1][1]:
                    antinode_one_y = pair[0][1] - i*y_diff
                    antinode_two_y = pair[1][1] + i*y_diff
                else:
                    antinode_one_y = pair[0][1] + i*y_diff
                    antinode_two_y = pair[1][1] - i*y_diff
                if 0 <= antinode_one_x < x_bound and 0 <= antinode_one_y < y_bound:
                    antinodes.add((antinode_one_x, antinode_one_y))
                else:
                    node_one_out_of_bounds = True
                if 0 <= antinode_two_x < x_bound and 0 <= antinode_two_y < y_bound:
                    antinodes.add((antinode_two_x, antinode_two_y))
                else:
                    node_two_out_of_bounds = True
                if node_one_out_of_bounds and node_two_out_of_bounds or p1:
                    break
                i += 1
                
    return antinodes


an, an2 = get_antinodes(lines, True), get_antinodes(lines, False)

print(f"p1: {len(an)}, p2: {len(an2)}")