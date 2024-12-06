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


def path_guard(obstacles, guard, lines, direction):
    stuck, traversed, visited = 0, set(), set()

    while True:
            obstacles_in_the_way = []
            if direction == ">":
                obstacles_in_the_way = sorted([obstacle for obstacle in obstacles if obstacle[0] > guard[0] and obstacle[1] == guard[1]], key=lambda x: x[0])
                if not obstacles_in_the_way:
                    for x in range(guard[0], len(lines[0])):
                        traversed.add((x, guard[1]))
                    break
                for x in range(guard[0], obstacles_in_the_way[0][0]):
                    traversed.add((x, guard[1]))
                guard = (obstacles_in_the_way[0][0]-1, guard[1])
                direction = "v"
                if (obstacles_in_the_way[0][0], obstacles_in_the_way[0][1], ">") not in visited:
                    visited.add((obstacles_in_the_way[0][0], obstacles_in_the_way[0][1], ">"))
                else:
                    stuck += 1
                    break
            elif direction == "<":
                obstacles_in_the_way = sorted([obstacle for obstacle in obstacles if obstacle[0] < guard[0] and obstacle[1] == guard[1]], key=lambda x: x[0], reverse=True)
                if not obstacles_in_the_way:
                    for x in range(guard[0], 0):
                        traversed.add((x, guard[1]))
                    break
                for x in range(guard[0], obstacles_in_the_way[0][0], -1):
                    traversed.add((x, guard[1]))
                guard = (obstacles_in_the_way[0][0]+1, guard[1])
                direction = "^"
                if (obstacles_in_the_way[0][0], obstacles_in_the_way[0][1], "<") not in visited:
                    visited.add((obstacles_in_the_way[0][0], obstacles_in_the_way[0][1], "<"))
                else:
                    stuck += 1
                    break
            elif direction == "^":
                obstacles_in_the_way = sorted([obstacle for obstacle in obstacles if obstacle[1] < guard[1] and obstacle[0] == guard[0]], key=lambda x: x[1], reverse=True)
                if not obstacles_in_the_way:
                    for y in range(guard[1], 0):
                        traversed.add((guard[0], y))
                    break
                for y in range(guard[1], obstacles_in_the_way[0][1], -1):
                    traversed.add((guard[0], y))
                guard = (guard[0], obstacles_in_the_way[0][1]+1)
                direction = ">"
                if (obstacles_in_the_way[0][0], obstacles_in_the_way[0][1], "^") not in visited:
                    visited.add((obstacles_in_the_way[0][0], obstacles_in_the_way[0][1], "^"))
                else:
                    stuck += 1
                    break
            elif direction == "v":
                obstacles_in_the_way = sorted([obstacle for obstacle in obstacles if obstacle[1] > guard[1] and obstacle[0] == guard[0]], key=lambda x: x[1])
                if not obstacles_in_the_way:
                    for y in range(guard[0], len(lines)):
                        traversed.add((guard[0], y))
                    break
                for y in range(guard[1], obstacles_in_the_way[0][1]):
                    traversed.add((guard[0], y))
                guard = (guard[0], obstacles_in_the_way[0][1]-1)
                direction = "<"
                if (obstacles_in_the_way[0][0], obstacles_in_the_way[0][1], "v") not in visited:
                    visited.add((obstacles_in_the_way[0][0], obstacles_in_the_way[0][1], "v"))
                else:
                    stuck += 1
                    print(f"found stuck at {x}, {y}")
                    break
            if not obstacles_in_the_way:
                break
    return stuck, len(traversed)

stuck = 0
for (x,y) in possible_obstacles:
    round = 0
    path_stuck, traversed = path_guard(obstacles+[(x, y)], guard, lines, direction=lines[guard[1]][guard[0]])
    stuck += path_stuck

_, traversed = path_guard(obstacles, guard, lines, direction=lines[guard[1]][guard[0]])    
print(f"Part 1: {traversed}, Part 2: {stuck}")