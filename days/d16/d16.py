lines = list(map(list, open("input.txt").read().splitlines()))

def rotation_cost(v1, v2):
    if v1 == tuple(-x for x in v2): # Opposite direction
        return 2000
    elif sum(a * b for a, b in zip(v1, v2)) == 0: # Perpendicular directions
        return 1000
    else:
        return 0

def parse_start():
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                return (j, i)


def bfs(_map, start, rotation_cost):
    q = [(*start, (1, 0), 0, [start])]
    visited = {}
    finished = []
    while q:
        x, y, prev_direction, steps, path = q.pop(0)
        if (x, y) in visited and visited[(x, y)][0] < (steps - 1000):
            continue
        if _map[y][x] == 'E':
            finished.append((steps, path))
            continue
        visited[(x, y)] = (steps, path)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in path:
                continue
            if 0 <= nx < len(_map[0]) and 0 <= ny < len(_map[0]) and _map[ny][nx] in 'E.':
                q.append((nx, ny, (dx, dy), steps + 1 + rotation_cost(prev_direction, (dx, dy)), path + [(nx, ny)]))
                
    return finished


finished = bfs(lines, parse_start(), rotation_cost)

p1 = min([f[0] for f in finished])
p2 = len(set([(x, y) for f in finished if f[0] == p1 for x, y in f[1]]))

print(f"Part 1: {p1}, Part 2: {p2}")