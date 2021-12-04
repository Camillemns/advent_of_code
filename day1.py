# part 1
with open('./input_day_1.txt') as file:
    input = file.read().splitlines()
    input = [int(ele) for ele in input]


def count_incre(l):
    count_incr = 0
    for i in range(1, len(l)):
        if l[i - 1] - l[i] < 0:
            count_incr += 1
    return count_incr


print('part 1 : {}'.format(count_incre(input)))


def sliding_window_sum(l, s=3):
    sliding_list = []
    for i in range(len(l) - (s-1)):
        sliding = 0
        for j in range(s):
            sliding += l[i+j]
        sliding_list.append(sliding)
    return sliding_list


print('part 2 : {}'.format(count_incre(sliding_window_sum(input))))
