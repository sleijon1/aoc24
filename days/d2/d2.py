lines = [list(map(int, line.split(" "))) for line in open("input.txt").read().splitlines()]

def check_safe(lines):
    safe_reports = 0
    unsafe_lines = []

    for line in lines:
        increasing, decreasing, diff_req = 0, 0, 0
        
        for i in range(len(line)):
            diff = line[i] - line[i-1] if i > 0 else 0
            if diff > 0:
                increasing += 1
            elif diff < 0:
                decreasing += 1
            if 1 <= abs(diff) <= 3:
                continue
            elif i > 0:
                diff_req += 1
                break
        if not (increasing and decreasing) and diff_req < 1:
            safe_reports += 1
        else:
            unsafe_lines.append(line)
    return safe_reports, unsafe_lines

safe_reports, unsafe_lines = check_safe(lines)
print(f"p1: {safe_reports}")
for line in unsafe_lines:
    alterations = [line[:i] + line[i+1:] for i in range(len(line))]
    sf, _ = check_safe(alterations)
    safe_reports += bool(sf)
print(f"p2: {safe_reports}")lines = open("input.txt").read().splitlines()
