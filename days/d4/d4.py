import numpy as np

lines = open("input.txt").read().splitlines()

def get_searches(strings):
    grid = np.array([list(row) for row in strings])
    horizontal = ["".join(row) for row in grid]
    vertical = ["".join(col) for col in grid.T]
    diagonals_tl_br = ["".join(np.diag(grid, k)) for k in range(-grid.shape[0] + 1, grid.shape[1])]
    flipped_grid = np.fliplr(grid)
    diagonals_tr_bl = ["".join(np.diag(flipped_grid, k)) for k in range(-flipped_grid.shape[0] + 1, flipped_grid.shape[1])]
    return [horizontal, vertical, diagonals_tl_br, diagonals_tr_bl]

xmas = 0
for search in get_searches(lines):
    for row in search:
        for i in range(len(row)):
            if row[i:i+4] in ("XMAS", "SAMX"):
                xmas += 1

x_mas, pattern = 0, ("SAM", "MAS")
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[i])-1):
        first_diag = lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1]
        second_diag = lines[i-1][j+1] + lines[i][j] + lines[i+1][j-1]
        if first_diag in pattern and second_diag in pattern:
            x_mas += 1

print(f"p1: {xmas}")
print(f"p2: {x_mas}")
