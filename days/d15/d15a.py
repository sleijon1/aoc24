storage, moves = open("input.txt").read().split("\n\n")
storage = list(map(list, storage.splitlines()))
moves = list("".join(moves.splitlines()))
robot = None
for i in range(len(storage)):
    for j in range(len(storage[i])):
        if storage[i][j] == "@":
            robot = (j, i)

def move_cascade(pos, v):
    next_pos = (pos[0] + v[0], pos[1] + v[1])
    if storage[next_pos[1]][next_pos[0]] == "#":
        return False
    elif storage[next_pos[1]][next_pos[0]] == "." or move_cascade(next_pos, v):
        storage[next_pos[1]][next_pos[0]] = storage[pos[1]][pos[0]]
        storage[pos[1]][pos[0]] = "."
        return True
    return False


def execute_moves(robot):
    while moves:
        move = moves.pop(0)
        move_dict = {
            "^": (0, - 1),
            "v": (0, 1),
            "<": (- 1, 0),
            ">": (1, 0)
        }
        moved = move_cascade(robot, move_dict[move])
        if moved:
            robot = (robot[0] + move_dict[move][0], robot[1] + move_dict[move][1])

def calc_storage(storage):
    sum = 0
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] == "O":
                sum += 100*i + j
    return sum

execute_moves(robot)
print(f"Part 1: {calc_storage(storage)}")