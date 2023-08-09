from pyfiglet import Figlet


def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()


def check_game1():
    # Vertical check 1
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("***The winner is: Player 1 (X)***")
        return True
    # Vertical check 2
    elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("***The winner is: Player 1 (X)***")
        return True
    # Vertical check 3
    elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("***The winner is: Player 1 (X)***")
        return True
    # Horizontal check 1
    elif game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("***The winner is: Player 1 (X)***")
        return True
    # Horizontal check 2
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("***The winner is: Player 1 (X)***")
        return True
    # Horizontal check 3
    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("***The winner is: Player 1 (X)***")
        return True
    # Cross check 1
    elif game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("***The winner is: Player 1 (X)***")
        return True
    # Cross check 2
    elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        print("***The winner is: Player 1 (X)***")
        return True
    return False


def check_game2():
    # Vertical check 1
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("***The winner is: Player 2 (O)***")
        return True
    # Vertical check 2
    elif game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print("***The winner is: Player 2 (O)***")
        return True
    # Vertical check 3
    elif game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        print("***The winner is: Player 2 (O)***")
        return True
    # Horizontal check 1
    elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("***The winner is: Player 2 (O)***")
        return True
    # Horizontal check 2
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("***The winner is: Player 2 (O)***")
        return True
    # Horizontal check 3
    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("***The winner is: Player 2 (O)***")
        return True
    # Cross check 1
    elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("***The winner is: Player 2 (O)***")
        return True
    # Cross check 2
    elif game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
        print("***The winner is: Player 2 (O)***")
        return True
    return False


f = Figlet(font='slant')
print(f.renderText('Tic-Tac-Toe'))

game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
show()

turns = 0

while True:
    # Player1
    print("Player 1: ")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game_board[row][col] == "-":
            game_board[row][col] = "X"
            show()
            if check_game1():
                break
            turns += 1
        else:
            print("That square has already been chosen! Choose another one.")
    else:
        print("You can only choose between 0 and 2.")

    # Check for tie
    if turns == 9:
        print("***No one wins!***")
        break

    # Player2
    print("Player 2: ")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game_board[row][col] == "-":
            game_board[row][col] = "O"
            show()
            if check_game2():
                break
            turns += 1
        else:
            print("That square has already been chosen! Choose another one.")
    else:
        print("You can only choose between 0 and 2.")

    # Check for tie
    if turns == 9:
        print("***No one wins!***")
        break
