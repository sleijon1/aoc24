import copy
from collections import defaultdict
lines = open("input.txt").read().splitlines()

trailheads = []
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "0":
            trailheads.append([(x, y)])


trailhead_nines, distinct_trails = defaultdict(set), 0
while trailheads:
    trail = trailheads.pop()
    if len(trail) == 10:
        distinct_trails += 1
        trailhead_nines[trail[0]].add(trail[-1])
        continue
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_trail = copy.copy(trail)
        cur_x, cur_y = trail[-1]
        new_x, new_y = cur_x + dx, cur_y + dy
        if new_y >= len(lines) or new_y < 0 or new_x >= len(lines[0]) or new_x < 0 or lines[new_y][new_x] == '.':
            continue
        if int(lines[new_y][new_x]) == int(lines[cur_y][cur_x]) + 1:
            new_trail.append((new_x, new_y))
            trailheads.append(new_trail)


print(f"p1 {sum([len(v) for k, v in trailhead_nines.items()])}, p2 {distinct_trails}")
