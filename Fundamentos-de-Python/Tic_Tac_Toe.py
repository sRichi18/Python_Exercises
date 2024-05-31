board = ["  " for i in range (9)]

def print_board():
    row1 = " | {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = " | {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = " | {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print("-" * 18)
    print(row2)
    print("-" * 18)
    print(row3)
    print()

def player_mov(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Is your turn player {}".format(number))
    selec = int(input("Choose your move (1-9): "))
    if board[selec - 1] == "  ":
        board[selec-1] = icon
    else:
        print()
        print("The space is occupied")

def winer(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[3] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def draw_game():
    if "  " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_mov("X")
    print_board()
    if winer("X"):
        print("X is the winer, congratulations")
        break
    elif draw_game():
        print("Draw game")
        break
    player_mov("O")
    if winer("O"):
        print("O is the winer, congratulations")
        break
    elif draw_game():
        print("Draw game")
        break
