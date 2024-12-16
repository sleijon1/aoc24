lines = list(map(list, open("input.txt").read().splitlines()))

rotation_cost = {
        ((0, 1), (1, 0)): 1000,
        ((1, 0), (0, 1)): 1000,
        ((0, -1), (1, 0)): 1000,
        ((1, 0), (0, -1)): 1000,
        ((0, 1), (-1, 0)): 1000,
        ((-1, 0), (0, 1)): 1000,
        ((0, -1), (-1, 0)): 1000,
        ((-1, 0), (0, -1)): 1000,
        ((0, -1), (0, 1)): 2000,
        ((0, 1), (0, -1)): 2000,
        ((1, 0), (-1, 0)): 2000,
        ((-1, 0), (1, 0)): 2000,
}

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
                r_cost = rotation_cost[(prev_direction, (dx, dy))] if prev_direction and prev_direction != (dx, dy) else 0
                q.append((nx, ny, (dx, dy), steps + 1 + r_cost, path + [(nx, ny)]))
                
    return finished


finished = bfs(lines, parse_start(), rotation_cost)

p1 = min([f[0] for f in finished])
p2 = len(set([(x, y) for f in finished if f[0] == p1 for x, y in f[1]]))

print(f"Part 1: {p1}, Part 2: {p2}")