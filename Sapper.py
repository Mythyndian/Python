import minesweeper


def sapper():
    rows = minesweeper.get_number(8, 25, 'Podaj liczbe wierszy (od 8 do 25): ')
    columns = minesweeper.get_number(8, 25, 'Podaj liczbe kolumn (od 8 do 20): ')
    number_of_mines = minesweeper.get_number(1, rows * columns - 1,
                                             f'Podaj liczbe min (od 1 do {rows * columns - 1}): ')
    mines = minesweeper.lay_mines(number_of_mines, rows, columns)
    board = minesweeper.create_board(mines, rows, columns)
    printable_fields = set()
    while len(printable_fields) < rows * columns - number_of_mines:
        minesweeper.print_board(board, rows, columns, printable_fields, print_all=False)
        i = minesweeper.get_number(0, rows - 1, f'Podaj numer wiersza (od {0} do {rows - 1}): ')
        j = minesweeper.get_number(0, columns, f'Podaj numer kolumn (od {0} do {rows - 1}): ')
        if (i, j) in mines:
            print('Przegrales!')
            minesweeper.print_board(board, rows, columns, printable_fields, print_all=True)
            break
        else:
            minesweeper.reveal_field((i, j), mines, board, rows, columns, printable_fields)


sapper()
