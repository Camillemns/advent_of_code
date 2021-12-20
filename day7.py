import numpy as np

with open('./input_day_7.txt') as file:
    input = file.read().split(',')
    input = [int(i) for i in input]

goal = np.median(input)

conso = 0
for i in input:
    conso += abs(goal - i)

print('part 1 : ' + str(conso))

goal = int(np.mean(input))
conso = 0
for i in input:
    n = abs(goal - i)
    conso += (n * (n + 1)) / 2

print('part 2 : ' + str(conso))