storage, moves = open("input.txt").read().split("\n\n")
storage = list(map(list, storage.splitlines()))
moves = list("".join(moves.splitlines()))
robot = None
double_storage = []
for i in range(len(storage)):
    double_row = []
    for j in range(len(storage[i])):
        if storage[i][j] == "@":
            robot = (len(double_row), i)
            double_row.append("@")
            double_row.append(".")
        elif storage[i][j] == "O":
            double_row.append("[")
            double_row.append("]")
        elif storage[i][j] == "#":
            double_row.append("#")
            double_row.append("#")
        elif storage[i][j] == ".":
            double_row.append(".")
            double_row.append(".")
    double_storage.append(double_row)


def move_cascade(pos, v, storage, moved=[]):
    next_pos = (pos[0] + v[0], pos[1] + v[1])
    if storage[next_pos[1]][next_pos[0]] == "#":
        return False
    elif storage[next_pos[1]][next_pos[0]] == ".":
        moved.append([(pos, next_pos), storage[pos[1]][pos[0]]])
        return True
    elif storage[next_pos[1]][next_pos[0]] in "[]" and v in [(0, -1), (0, 1)]:
        if  storage[next_pos[1]][next_pos[0]] == ".":
            return True
        elif storage[next_pos[1]][next_pos[0]] == "[":
            matching_bracket = (next_pos[0] + 1, next_pos[1])
        elif storage[next_pos[1]][next_pos[0]] == "]":
            matching_bracket = (next_pos[0] - 1, next_pos[1])

        if move_cascade(matching_bracket, v, storage, moved=moved) and move_cascade(next_pos, v, storage, moved=moved):
            moved.append([(next_pos, (next_pos[0] + v[0], next_pos[1] + v[1])), storage[next_pos[1]][next_pos[0]]])
            moved.append([(matching_bracket, (matching_bracket[0] + v[0], matching_bracket[1] + v[1])), storage[matching_bracket[1]][matching_bracket[0]]])
            moved.append([(pos, next_pos), storage[pos[1]][pos[0]]])
            return True

        return False
    elif storage[next_pos[1]][next_pos[0]] in "[]" and v in [(1, 0), (-1, 0)]:
        if move_cascade(next_pos, v, storage, moved=moved):
            moved.append([(pos, next_pos), storage[pos[1]][pos[0]]])
            return True
        return False

def execute_moves(robot, storage):
    while moves:
        move = moves.pop(0)
        move_dict = {"^": (0, - 1), "v": (0, 1), "<": (- 1, 0), ">": (1, 0)}
        cascade = []
        moved = move_cascade(robot, move_dict[move], storage, moved=cascade)
        checked = []
        if moved:
            for m, tok in cascade:
                if m[0] in checked:
                    continue
                checked.append(m[0])
                storage[m[1][1]][m[1][0]] = tok
                storage[m[0][1]][m[0][0]] = "."
            robot = (robot[0] + move_dict[move][0], robot[1] + move_dict[move][1])
        
        
def calc_storage(storage):
    sum = 0
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] == "[":
                sum += 100*i + j
    return sum

execute_moves(robot, double_storage)
print(f"Part 2: {calc_storage(double_storage)}")
