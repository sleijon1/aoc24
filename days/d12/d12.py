from collections import defaultdict
from itertools import combinations
lines = list(map(list, open("input.txt").read().splitlines()))

def check_match(p1, p2):
    return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) == 1) and (lines[p1[1]][p1[0]] == lines[p2[1]][p2[0]]) 

def calculate_region(lines):
    final_regions = []
    moved = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (j, i) in moved:
                continue
            queue = [(j, i)]
            region = []
            while queue:
                c = queue.pop()
                if c in region:
                    continue
                region.append(c)
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= c[1] + d[1] < len(lines) and 0 <= c[0] + d[0] < len(lines[0]) and check_match(c, (c[0] + d[0], c[1] + d[1])):
                        queue.append((c[0] + d[0], c[1] + d[1]))
                        moved.append((c[0] + d[0], c[1] + d[1]))
            final_regions.append(region)
    return final_regions

def calculate_perim(region):
    perim = set()
    for r in region:
        for d in [(0, 1, 'd'), (0, -1, 'u'), (1, 0, 'r'), (-1, 0, 'l')]:
            if (r[0] + d[0], r[1] + d[1]) not in region:
                perim.add((r[0] + d[0], r[1] + d[1], d[2]))
    return perim

def calculate_sides(perim):
    sides = []
    perim = sorted([node for node in perim if node[2] in ['u', 'd']], key=lambda x: x[0]) \
          + sorted([node for node in perim if node[2] in ['l', 'r']], key=lambda x: x[1])
    while perim:
        node = perim.pop()
        found = False
        for side in sides:
            for node_2 in side:
                if node[2] in ['l', 'r']:
                    for d in [(0, 1), (0, -1)]:
                        if (node[0] + d[0], node[1] + d[1], node[2]) == node_2:
                            found = True
                            break
                elif node[2] in ['u', 'd']:
                    for d in [(1, 0), (-1, 0)]:
                        if (node[0] + d[0], node[1] + d[1], node[2]) == node_2:
                            found = True
                            break
            if found:
                break
        if not found:
            sides.append([node])
        elif found:
            side.append(node)
    return sides
                

def calculate_price(regions, discount=False):
    price = 0
    for region in regions:
        perim = len(calculate_perim(region)) if not discount else len(calculate_sides(calculate_perim(region)))
        area = len(region)
        price += perim * area
    
    return price

final_regions = calculate_region(lines)
print(f"p1: {calculate_price(final_regions)} p2: {calculate_price(final_regions, discount=True)}", )