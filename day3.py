import numpy as np
from collections import Counter

with open('./input_day_3.txt') as file:
    input = file.read().splitlines()


def prepare(input):
    a = np.zeros((len(input[0]), len(input)))
    for i in range(len(input[0])):
        for j in range(len(input)):
            a[i][j] = int(input[j][i])
    return a


def count(input):
    liste = prepare(input)
    comm = []
    for i in range(len(input[0])):
        occ = Counter(liste[:][i])
        comm.append(occ.most_common())
    return comm


gamma_rate = []
epsilon_rate = []
for i in range(len(input[0])):
    comm = count(input)
    gamma_rate.append(comm[i][0][0])
    epsilon_rate.append(comm[i][-1][0])
most_common = ''.join([str(int(i)) for i in gamma_rate])
least_common = ''.join([str(int(i)) for i in epsilon_rate])

print('gamma : {}'.format(most_common))
print('epsilon : {}'.format(least_common))
print('gamma decimal: {}'.format(int(most_common, 2)))
print('epsilon decimal: {}'.format(int(least_common, 2)))
print('part 1 : {}'.format(int(least_common, 2) * int(most_common, 2)))


def rating(n_bit, lst, least=True):
    same, id = ('0', -1) if least else ('1', 0)
    for i in range(n_bit):
        m = str(int(count(lst)[i][id][0]))
        if count(lst)[i][0][1] == count(lst)[i][-1][1]:
            m = same
        lst = [n for n in lst if n[i] == m]
        if len(lst) == 1:
            rating = lst[0]
            return rating


co2_rating = rating(len(least_common), input)
ox_rating = rating(len(most_common), input, least=False)
print('co2 rating: {}'.format(co2_rating))
print('oxygen rating: {}'.format(ox_rating))
print('co2 rating decimal: {}'.format(int(co2_rating, 2)))
print('oxygen rating decimal: {}'.format(int(ox_rating, 2)))
print('part 2 : {}'.format(int(ox_rating, 2) * int(co2_rating, 2)))
