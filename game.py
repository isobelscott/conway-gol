from random import choices
import emoji


class Game:
    # generate initial board
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.board = [[choices([0,0,0,1])[0] for _ in range(cols)] for _ in range(rows)]

    def get_valid_neighbors(self, i, j):
        cell = [i, j]
        potential_neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        valid_neighbors = []
        for pot in potential_neighbors:
            pot_neigh = [pot[0] + cell[0], pot[1] + cell[1]]
            if (self.rows > pot_neigh[0] > -1) and (self.cols > pot_neigh[1] > -1):
                valid_neighbors.append(pot_neigh)
        return valid_neighbors

    def next_gen(self):
        next_gen_alive = []
        new_board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.board[i][j]
                neighbors = self.get_valid_neighbors(i, j)
                live_neighbors = sum(self.board[coor[0]][coor[1]] for coor in neighbors)
                if live_neighbors == 3:
                    next_gen_alive.append([i, j])
                if cell == 1 and live_neighbors == 2:
                    next_gen_alive.append([i, j])

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if [i, j] in next_gen_alive:
                    new_board[i][j] = 1

        self.board = new_board

        new_board = [[emoji.emojize(':alien_monster:') if x == 1 else " " for x in l] for l in new_board]

        return new_board
