import random

class Sudoku:
    def __init__(self):
        self.board = ['_' for i in range(81)]

    def available_positions(self):
        return [i for i, spot in enumerate(self.board) if spot == '_']

    def find_next_empty(self):
        for i in self.available_positions():
            return i

    def show_board(self):
        for i in range(0, 81, 9):
            show = '| '
            for x in range(9):
                show = show + str(self.board[i+x]) + ' | '
            print(show)

    def valid_small(self, position, random_number):
        # check if the given number meets the small square criteria
        col = position % 9
        row = position // 9
        row_low = row // 3 * 3
        col_low = col // 3 * 3
        first_position = (row_low * 9) + col_low
        small_box = []
        for i in [0, 1, 2]:
            for x in [0, 9, 18]:
                small_box.append(self.board[first_position + i + x])
        if random_number in small_box:
            return False
        else:
            return True

    def valid_big(self, position, random_number):
        # check if the given number meets the big square criteria
        row = position // 9
        row_numbers = self.board[row*9 : row*9+9]

        column = position % 9
        column_numbers = self.board[column: 81: 9]

        if random_number in row_numbers:
            return False
        elif random_number in column_numbers:
            return False
        else:
            return True

    def set_numbers(self):
        position = random.choice(self.available_positions())
        random_number = random.randint(1,9)
        if self.valid_small(position, random_number) and self.valid_big(position, random_number):
            self.board[position] = random_number
        else:
            self.set_numbers()

    def create_board(self, given_numbers):
        self.given_numbers = given_numbers
        for i in range(self.given_numbers):
            self.set_numbers()
        self.show_board()

    def solve_board(self):
        pos = self.find_next_empty()

        if pos is None:
            return True

        for num in range(1, 10):
            if self.valid_small(pos, num) and self.valid_big(pos, num) and self.board[pos] == '_':
                self.board[pos] = num

                # recursively call our function
                if self.solve_board():
                    return True

            self.board[pos] = '_'

        # if none of the numbers that we try work, then this board is unsolvable
        return False



if __name__ == '__main__':
    game = Sudoku()
    print("The board is:")
    game.create_board(15)
    print("Solved board:")
    if game.solve_board():
        game.show_board()
    else:
        print("This board is unsolvable")



