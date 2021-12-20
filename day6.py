with open('./input_day_6.txt') as file:
    input = file.read().split(',')
    input = [int(i) for i in input]

fish_days = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in input:
    fish_days[i] += 1

def reset_cycle(fish_days):
    r_cycle = fish_days[0]
    temp = fish_days[1:]
    temp.append(r_cycle)
    temp[6] += r_cycle
    return temp

days = 80
for i in range(days) :
    fish_days = reset_cycle(fish_days)

print('day 1 : '.format(sum(fish_days)))

for i in range(256 - days) :
    fish_days = reset_cycle(fish_days)

print('day 2 : '.format(sum(fish_days)))