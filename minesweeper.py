import random


def get_number(a, b, text):
    while True:
        number = int(input(text))
        if a <= number <= b:
            return number
        else:
            print(f"Podaj liczbe calkowita z zakresu {a} - {b}")


def lay_mines(number_of_mines, rows, columns):
    mines = set()
    while len(mines) < number_of_mines:
        i = random.randrange(rows)
        j = random.randrange(columns)
        mines.add((i, j))
    return mines


def number_of_neighboring_mines(filed, mines, rows, columns):
    count = 0
    i = filed[0]
    j = filed[1]

    for m, n in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                 (i, j - 1), (i, j + 1),
                 (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
        if 0 <= m < rows and 0 <= n < columns and (m, n) in mines:
            count += 1

    return count


def create_board(mines, rows, columns, mine='*'):
    board = []

    for i in range(rows):
        row = []
        for j in range(columns):
            if (i, j) in mines:
                row.append(mine)
            else:
                row.append(number_of_neighboring_mines(
                    (i, j), mines, rows, columns))
        board.append(row)

    return board


def print_board(board, rows, columns, printables_fields, print_all=False):
    print('   ', end='')
    for i in range(columns):
        print(f"{i:^4}", end='')
    print()
    for i in range(rows):
        print(f"{i:^3}", end='')
        for j in range(columns):
            if (i, j) in printables_fields:
                print(f"{board[i][j]:^3}|", end='')
            else:
                print(f"{'#':^3}|", end='')
        print()


def reveal_field(field, mines, board, rows, columns, printable_fields):
    i = field[0]
    j = field[1]

    if (not(0 <= i < rows and 0 <= j < columns)) or field in printable_fields:
        return
    printable_fields.add((i, j))

    if board[i][j] == 0:
        return
