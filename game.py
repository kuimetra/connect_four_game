import numpy as np


def is_sub_array(a, id):
    b = [id] * 4
    n, m, i, j = len(a), len(b), 0, 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            i = i - j + 1
            j = 0
    return False


class Connect4:
    def __init__(self):
        self.grid = [[0] * 6 for _ in range(7)]
        self.player_id = 1
        self.game_over = False

    def get_grid(self):
        return list(np.rot90(self.grid).flatten())

    def get_amount_of_filled_cells(self, col):
        return len([*filter(lambda x: x != 0, self.grid[col])])

    @staticmethod
    def get_diag(grid):
        return [grid.diagonal(i) for i in range(-3, 5)]

    def any_match(self, grid):
        return any(is_sub_array(col, self.player_id) for col in grid)

    def check_match(self):
        rotated_grid = np.rot90(self.grid)
        diagonals, anti_diagonals = self.get_diag(rotated_grid), self.get_diag(np.fliplr(rotated_grid))
        col_match, row_match = self.any_match(self.grid), self.any_match(rotated_grid)
        diag_match, anti_diag_match = self.any_match(diagonals), self.any_match(anti_diagonals)
        return col_match or row_match or diag_match or anti_diag_match

    def make_move(self, col):
        self.grid[col].pop()
        self.grid[col].insert(self.get_amount_of_filled_cells(col), self.player_id)

    def pass_turn(self):
        if self.player_id == 1:
            self.player_id = 2
        elif self.player_id == 2:
            self.player_id = 1
