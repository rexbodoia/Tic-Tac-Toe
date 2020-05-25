#!./anaconda/bin/python
import random

SIZE=3
SYMBOLS=['X','O']

def print_grid(grid):
    print(f' {grid[0][0]} | {grid[0][1]} | {grid[0][2]} ')
    print('-----------')
    print(f' {grid[1][0]} | {grid[1][1]} | {grid[1][2]} ')
    print('-----------')
    print(f' {grid[2][0]} | {grid[2][1]} | {grid[2][2]} ')

def create_grid():
    grid = []
    for row in range(SIZE):
        row = []
        for col in range(SIZE):
            row.append(' ')
        grid.append(row)
    return grid

def ask_for_symbol():
    def get_symbol():
        return input(f"Please choose a symbol by typing '{SYMBOLS[0]}' or '{SYMBOLS[1]}': ")
    symbol = get_symbol()
    while not symbol in SYMBOLS:
        print(f'Invalid symbol. Please choose {SYMBOLS[0]} or {SYMBOLS[1]}')
        symbol = ask_for_symbol()
    return symbol

def opposite_symbol(symbol):
    if symbol == SYMBOLS[0]:
        return SYMBOLS[1]
    else:
        return SYMBOLS[0]

def player_move(symbol, grid):
    def get_move():
        choice = input(f"{symbol}'s turn. Please choose a row,col: ").strip()
        inputs = choice.split(',')
        for i in inputs:
            i.strip()
        try:
            row = int(inputs[0])
            col = int(inputs[1])
        except:
            print('Invalid row,col. Please choose again')
            row, col = get_move()
        return row, col
    row, col = get_move()
    while grid[row][col] != ' ':
        row, col = get_move()
    grid[row][col] = symbol

def computer_move(symbol, grid):
    def get_move():
        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)
        return row, col
    row, col = get_move()
    while not is_over(grid) and grid[row][col] != ' ':
        row, col = get_move()
    grid[row][col] = symbol

def check_for_row(symbol, grid):
    any_rows = False
    for row in grid:
        still_valid = True
        for col in row:
            if col != symbol:
                still_valid = False
        if still_valid:
            any_rows = True
    return any_rows

def check_for_col(symbol, grid):
    any_cols = False
    for col in range(SIZE):
        still_valid = True
        for row in grid:
            if row[col] != symbol:
                still_valid = False
        if still_valid:
            any_cols = True
    return any_cols

def check_for_diagonal(symbol, grid):
    first_diagonal = False
    still_valid = True
    for i in range(SIZE):
        if grid[i][i] != symbol:
            still_valid = False
    first_diagonal = still_valid
    second_diagonal = False
    still_valid = True
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            if row_idx + col_idx == len(grid) - 1:
                if grid[row_idx][col_idx] != symbol:
                    still_valid == False
    second_diagonal = still_valid
    return first_diagonal or second_diagonal

def three_in_a_row(symbol, grid):
    in_row = check_for_row(symbol, grid)
    in_col = check_for_col(symbol, grid)
    in_diagonal = check_for_diagonal(symbol, grid)
    return in_row or in_col or in_diagonal

def full_grid(grid):
    for row in grid:
        for col in row:
            if col == ' ':
                return False
    return True

def is_over(grid):
    if full_grid(grid):
        return True
    else:
        for symbol in SYMBOLS:
            if three_in_a_row(symbol, grid):
                return True
        return False

if __name__ == "__main__":
    grid = create_grid()
    print_grid(grid)
    player_symbol = ask_for_symbol()
    computer_symbol = opposite_symbol(player_symbol)

    while not is_over(grid):
        player_move(player_symbol, grid)
        computer_move(computer_symbol, grid)
        print_grid(grid)

    if three_in_a_row(player_symbol, grid):
        print("You Win!")
    elif three_in_a_row(computer_symbol, grid):
        print("You lost, maybe next time!")
    else:
        print("Stalemate!")
    print("Thanks for playing!")
