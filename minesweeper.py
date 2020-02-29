import random
def get_number(a, b, text):
    while True:
        number= int(input(text))
        if a<= number <=b:
            return number
        else:
            print(f"Podaj liczbê ca³kowit¹ z zakresu {a} - {b}")



def lay_mines(number_of_mines, rows, columns):
    mines= set()
    while len(mines) < number_of_mines:
        i= random.randrange(rows)
        j= random.randrange(columns)
        mines.add((i,j))
    return mines

def number_of_neighboring_mines(filed, mines, rows, columns):
    count =0
    i=filed[0]
    j=filed[1]

    for m,n in [(i-1,j-1),(i-1,j),(i-1,j+1),
                (i,j-1),(i,j+1),
                (i+1,j-1),(i+1,j),(i+1,j+1)]:
        if 0 <= m < rows and 0 <= n < columns and (m,n) in mines:

            count += 1

    return count

def create_board(mines, rows, columns, mine = '*'):
    board= []

    for i in range(rows):
        row =[]
        for j in range(columns):
            if(i,j) in mines:
                row.append(mine)
            else:
                row.append(number_of_neighboring_mines(
                    (i,j),mines, rows, columns))
        board.append(row)

    return board

number_of_mines = 30
rows = 10
columns = 10
mines= lay_mines(number_of_mines, rows, columns)
board = create_board(mines, rows, columns)

for row in board:
    for el in row:
        print(f"{el:^3}", end = '')
    print()
