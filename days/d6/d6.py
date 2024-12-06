from copy import deepcopy
lines = [list(line) for line in open("input.txt").read().splitlines()]
obstacles, guard, possible_obstacles = [], None, []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            obstacles.append((x, y)) 
        elif c in ('>', '<', '^', 'v'):
            guard = (x, y)
        elif c == ".":
            possible_obstacles.append((x, y))


original_obstacles = deepcopy(obstacles)
original_guard = guard
original_lines = deepcopy(lines)

def path_guard(obstacles, guard, lines):
    traversed = set()
    stuck = 0
    round = 0
    while True:
            obstacles_in_the_way = []
            if lines[guard[1]][guard[0]] == ">":
                obstacles_in_the_way = sorted([obstacle for obstacle in obstacles if obstacle[0] > guard[0] and obstacle[1] == guard[1]], key=lambda x: x[0])
                if not obstacles_in_the_way:
                    for x in range(guard[0], len(lines[0])):
                        traversed.add((x, guard[1]))
                    break
                for x in range(guard[0], obstacles_in_the_way[0][0]):
                    traversed.add((x, guard[1]))
                guard = (obstacles_in_the_way[0][0]-1, guard[1])
                lines[guard[1]][guard[0]] = "v"
            elif lines[guard[1]][guard[0]] == "<":
                obstacles_in_the_way = sorted([obstacle for obstacle in obstacles if obstacle[0] < guard[0] and obstacle[1] == guard[1]], key=lambda x: x[0], reverse=True)
                if not obstacles_in_the_way:
                    for x in range(guard[0], 0):
                        traversed.add((x, guard[1]))
                    break
                for x in range(guard[0], obstacles_in_the_way[0][0], -1):
                    traversed.add((x, guard[1]))
                guard = (obstacles_in_the_way[0][0]+1, guard[1])
                lines[guard[1]][guard[0]] = "^"
            elif lines[guard[1]][guard[0]] == "^":
                obstacles_in_the_way = sorted([obstacle for obstacle in obstacles if obstacle[1] < guard[1] and obstacle[0] == guard[0]], key=lambda x: x[1], reverse=True)
                if not obstacles_in_the_way:
                    for y in range(guard[1], 0):
                        traversed.add((guard[0], y))
                    break
                for y in range(guard[1], obstacles_in_the_way[0][1], -1):
                    traversed.add((guard[0], y))
                guard = (guard[0], obstacles_in_the_way[0][1]+1)
                lines[guard[1]][guard[0]] = ">"
            elif lines[guard[1]][guard[0]] == "v":
                obstacles_in_the_way = sorted([obstacle for obstacle in obstacles if obstacle[1] > guard[1] and obstacle[0] == guard[0]], key=lambda x: x[1])
                if not obstacles_in_the_way:
                    for y in range(guard[0], len(lines)):
                        traversed.add((guard[0], y))
                    break
                for y in range(guard[1], obstacles_in_the_way[0][1]):
                    traversed.add((guard[0], y))
                guard = (guard[0], obstacles_in_the_way[0][1]-1)
                lines[guard[1]][guard[0]] = "<"
            if not obstacles_in_the_way:
                break
            if round > 300:
                stuck += 1
                print(f"found stuck at {x}, {y}")
                break
            round += 1
    return stuck, len(traversed)

stuck = 0
for (x,y) in possible_obstacles:
    obstacles = deepcopy(original_obstacles)
    obstacles.append((x, y))
    round = 0
    guard = original_guard
    lines = deepcopy(original_lines)
    path_stuck, traversed = path_guard(obstacles, guard, lines)
    stuck += path_stuck

_, traversed = path_guard(deepcopy(original_obstacles), original_guard, deepcopy(original_lines))    
print(f"Part 1: {traversed}, Part 2: {stuck}")