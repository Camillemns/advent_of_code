import numpy as np


class Board():
    def __init__(self, n, numbers):
        self.size = n
        self.board = np.zeros((n, n))
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                self.board[i][j] = numbers[i][j]
        self.marked = np.zeros((n, n))

    def mark(self, d):
        position_of_draw = np.where(self.board == d)
        coordinates = list(zip(position_of_draw[0], position_of_draw[1]))
        for (i, j) in coordinates:
            self.marked[i, j] = 1

    def check(self, axis):
        sum = self.marked.sum(axis=axis)
        if np.any(sum == self.size):
            return True
        else:
            return False

    def sum_unmarked(self):
        positions = np.where(self.marked == 0)
        coordinates = list(zip(positions[0], positions[1]))
        sum = 0
        for (i, j) in coordinates:
            sum += self.board[i][j]
        return sum

    def check_bingo(self):
        row_bingo = self.check(0)
        col_bingo = self.check(1)
        if col_bingo or row_bingo:
            return self.sum_unmarked()
        else:
            return False


def prepare():
    with open('./input_day_4.txt') as file:
        input = file.read().splitlines()
    drawns = [int(i) for i in input[0].split(',')]
    numbers_in_boards = [[int(ele) for ele in i.split()] for i in input[1:]]
    boards = []
    n = 5
    i = 0
    while i < len(numbers_in_boards):
        if not numbers_in_boards[i]:
            i = i+1
        else:
            boards.append(Board(n, numbers_in_boards[i:i+n]))
            i = i+n
    return drawns, boards


def draw(d, boards):
    scores, id_wins, turn_wins = [], [], []
    for turn, ele in enumerate(d):
        for i in range(len(boards)):
            if i not in id_wins:
                boards[i].mark(ele)
                is_bingo = boards[i].check_bingo()
                if is_bingo:
                    score = is_bingo * ele
                    scores.append(score)
                    turn_wins.append(turn)
                    id_wins.append(i)
    return scores, turn_wins


def last_win(id_wins):
    return id_wins[-1]


# prepare
drawns, boards = prepare()
# part1
score, turn_wins = draw(drawns, boards)
print('part 1 : Score of first to win :'.format(score[0]))
# part 2
print('part 2 : Score of last to win : '.format(score[-1]))
