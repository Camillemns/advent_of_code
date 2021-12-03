with open('./input_day_2.txt') as file :
    input = file.read().splitlines()

def part1(i):
    horizontal = 0
    depth = 0
    for ele in i:
        d = next((int(s) for s in ele.split() if s.isdigit()), None)
        if 'forward' in ele:
            horizontal += d
        elif 'down' in ele:
            depth += d
        else :
            depth -= d
    return depth, horizontal


d, h = part1(input)
print('part 1 : {}'.format(d * h))


def part1(i):
    horizontal = 0
    depth = 0
    aim = 0
    for ele in i:
        d = next((int(s) for s in ele.split() if s.isdigit()), None)
        if 'forward' in ele:
            horizontal += d
            depth += aim * d
        elif 'down' in ele:
            aim += d
        else :
            aim -= d
    return depth, horizontal, aim


d, h, a = part1(input)
print('part 2 : {}'.format(d * h))