with open('./input_day_8.txt') as file:
    input = file.read().splitlines()
    input = [i.split(' ') for i in input]


unique_len = [2, 4, 3, 7]
count = 0
for i in input:
    for j in i[-4:]:
        if j != '|':
            if len(j) in unique_len:
                count += 1

print('part 1: ' + str(count))

sum = 0
for i in input:
    map_list = {}
    digits = i[:-5]
    map_list[1] = [d for d in digits if len(d) == 2][0]
    map_list[7] = [d for d in digits if len(d) == 3][0]
    map_list[4] = [d for d in digits if len(d) == 4][0]
    map_list[8] = [d for d in digits if len(d) == 7][0]
    for v in map_list.values():
        digits.remove(v)
    five_bar = [d for d in digits if len(d) == 5]
    six_bar = [d for d in digits if len(d) == 6]
    for d in six_bar:
        if len(list(set(map_list[4]).intersection(d))) == 4:
            map_list[9] = d
        elif len(list(set(map_list[4]).intersection(d))) == 3 and len(list(set(map_list[7]).intersection(d))) == 3:
            map_list[0] = d
        else :
            map_list[6] = d
    for d in five_bar:
        if len(list(set(map_list[1]).intersection(d))) == 2:
            map_list[3] = d
        elif len(list(set(map_list[9]).intersection(d))) == 4:
            map_list[2] = d
        else :
            map_list[5] = d
    inv_map = {''.join(sorted(v)): k for k, v in map_list.items()}
    d = i[-4:]
    digit = ''
    for i in range(4):
        digit += str(inv_map[''.join(sorted(d[i]))])
    sum += int(digit)

print('part 2: ' + str(sum))