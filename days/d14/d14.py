import re
import math
from time import sleep
import matplotlib.pyplot as plt
from collections import defaultdict

lines = open("input.txt").read().splitlines()
robots = []
for line in lines:
    digits = re.findall("-?\d+", line)
    robots.append([[int(digits[0]), int(digits[1])], (int(digits[2]), int(digits[3]))])

def calculate_safety_vector():
    quadrants = [[], [], [], []]

    for robot in robots:
        x, y = robot[0]
        if x < (wide // 2) and y < (tall // 2):
            quadrants[0].append(robot)
        elif x > (wide // 2) and y < (tall // 2):
            quadrants[1].append(robot)
        elif x < (wide // 2) and y > (tall // 2):
            quadrants[2].append(robot)
        elif x > (wide // 2) and y > (tall // 2):
            quadrants[3].append(robot)

    return math.prod([len(q) for q in quadrants])

def save_image():
    """ To find the answer for part 2 you run this
    for every iteration up to some experimental second S
    and visualize the images somewhere to find the
    christmas tree. Turns out mine was on 6587th iteration (S=6587).
    So I hard code it to get both solutions with one run without 
    saving a bunch of images. """
    vis_lines = []
    rs = defaultdict(bool)
    rs.update({tuple(r[0]): True for r in robots})
    for y in range(tall):
        vis_line = []
        for x in range(wide):
            if rs[(x, y)]:
                vis_line.append(1)
            else:
                vis_line.append(2)
        vis_lines.append(vis_line)
    plt.imshow(vis_lines, cmap='viridis')
    plt.savefig((file_name := "christmas_tree.png"))
    print(f"part two saved in {file_name}")
    plt.close()

seconds, wide, tall = 6588, 101, 103
for i in range(seconds):
    if i == 6587:
        save_image()

    for robot in robots:
        new_x = robot[0][0] + robot[1][0]
        new_y = robot[0][1] + robot[1][1]
        if new_x < 0:
            new_x = new_x + wide
        elif new_x >= wide:
            new_x = abs(wide - new_x)
        if new_y < 0:
            new_y = new_y + tall
        elif new_y >= tall:
            new_y = abs(tall - new_y)
        robot[0] = [new_x, new_y]
    if i == 99:
        print("p1: ", calculate_safety_vector())
