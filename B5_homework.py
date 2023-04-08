board = list(range(1, 10))


def drawboard():
    print("\t     |     |")
    print(f"\t  {board[0]}  |  {board[1]}  |  {board[2]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {board[3]}  |  {board[4]}  |  {board[5]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("\t     |     |")


drawboard()


def take_input(player):
    while True:
        val = input('Куда ввести ' + player + ': ')
        if not val in '123456789':
            print('Неверный ввод. Повторите попытку')
            continue
        val = int(val)
        if str(board[val - 1]) in 'X0':
            print('Ячейка занята')
            continue
        board[val - 1] = player
        break


def check_winner():
    if any([board[0] == board[1] == board[2],
            board[3] == board[4] == board[5],
            board[6] == board[7] == board[8],
            board[0] == board[3] == board[6],
            board[1] == board[4] == board[7],
            board[2] == board[5] == board[8],
            board[0] == board[4] == board[8],
            board[2] == board[4] == board[6]]):
        return True
    else:
        return False


player1 = 'X'
player2 = '0'
count = 0
while count < 7:
    take_input(player1)
    drawboard()
    win = check_winner()
    if win == True:
        print('Выиграл игрок 1')
        break
    count = count + 1
    take_input(player2)
    drawboard()
    win = check_winner()
    if win == True:
        print('Выиграл игрок 2')
        break
    count = count + 1
if win == False:
    print('Ничья')
