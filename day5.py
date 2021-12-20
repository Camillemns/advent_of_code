import re
import numpy as np
from numpy.core.fromnumeric import argmin, take

with open('./input_day_5.txt') as file:
    input = file.read().splitlines()
    input = [list(filter(None, re.split(r'[^0-9.]', i))) for i in input]
    array = np.zeros((len(input), 4))
    for i in range(len(input)):
        for j in range(4):
            array[i][j] = int(input[i][j])
    maxes = array.max(axis=0)
    size_x = int(max(maxes[0], maxes[2]))
    size_y = int(max(maxes[1], maxes[3]))
    space = np.zeros((size_x + 1, size_y + 1))


def is_vertical(x1, y1, x2, y2):
    if x1 == x2:
        return True
    else:
        return False


def is_horizontal(x1, y1, x2, y2):
    if y1 == y2:
        return True
    else:
        return False


def is_diagonal(x1, y1, x2, y2):
    if abs(x1-x2) == abs(y1-y2):
        return True
    else:
        return False


def list_point(x1, y1, x2, y2):
    points = []
    if is_vertical(x1, y1, x2, y2):
        for i in range(int(abs(y1-y2)) + 1):
            y = min(y1, y2)
            points.append((x1, y + i))
    elif is_horizontal(x1, y1, x2, y2):
        for i in range(int(abs(x1-x2)) + 1):
            x = min(x1, x2)
            points.append((x + i, y1))
    return points


def list_point_dia(x1, y1, x2, y2):
    points = []
    if is_diagonal(x1, y1, x2, y2):
        m = round((y2-y1) / (x2-x1))
        c = y2-m*x2
        x = min(x1, x2)
        for i in range(int(abs(x1-x2)) + 1):
            points.append((x + i, round(m*(x + i) + c)))
        return points
    if is_vertical(x1, y1, x2, y2):
        for i in range(int(abs(y1-y2)) + 1):
            y = min(y1, y2)
            points.append((x1, y + i))
        return points
    if is_horizontal(x1, y1, x2, y2):
        for i in range(int(abs(x1-x2)) + 1):
            x = min(x1, x2)
            points.append((x + i, y1))
        return points


for p in array:
    points = list_point(p[0], p[1], p[2], p[3])
    for point in points:
        space[int(point[0])][int(point[1])] += 1

dangerous_area = (space > 1).sum()
print(dangerous_area)

space = np.zeros((size_x + 1, size_y + 1))
for p in array:
    points = list_point_dia(p[0], p[1], p[2], p[3])
    for point in points:
        space[int(point[0])][int(point[1])] += 1


dangerous_area = (space > 1).sum()
print(dangerous_area)
