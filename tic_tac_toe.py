import sys
from itertools import product
from random import choice

# create board
board_size = 3
board = [["-" for _ in range(board_size)] for _ in range(board_size)]


def is_board_filled(board):
    return all(
        "-" not in board[r][c] for r, c in product(range(board_size), range(board_size))
    )


def is_position_filled(board, position):
    x, y = position
    return board[x][y] != "-"


def show_board(board):
    for row in board:
        sys.stdout.write(f"{row[0]} {row[1]} {row[2]}\n")


def start_game():
    chosen_player = choice(["x", "o"])
    sys.stdout.write(
        "\nInstructions\n"
        + "------------------------------------------------------------------------------------------------------------\n"
        + "Hello, players! Welcome to the classic game, tic-tac-toe!\n"
        + 'To play, choose to be "x" or "o"\n'
        + "When it is your turn, enter the row and column in which you wish to put your character on the board.\n"
        + 'For example, if you wish to play in the first position from left to right, enter "0, 0" when prompted.\n'
        + "Note that row and column indices start from 0 and end at 2.\n"
        + "Now, let's have some fun!\n"
        + "------------------------------------------------------------------------------------------------------------\n"
    )

    # initialize gameplay loop
    while not is_board_filled(board):
        # show the board to the user and ask for a move
        sys.stdout.write(f"\nYour turn, {chosen_player}\n")
        show_board(board)
        position = get_player_input()
        if position == False:
            sys.stdout.write("Invalid input! Try again.\n")
            continue

        # if position is available, update the spot in the board
        if not is_position_filled(board, position):
            board[position[0]][position[1]] = chosen_player
        else:
            sys.stdout.write("Invalid move! Try again.\n")
            continue

        # check whether a player has won
        winner = get_winner(board)
        if winner:
            break

        # change player
        chosen_player = "o" if chosen_player == "x" else "x"

    sys.stdout.write("\n")
    show_board(board)
    if winner:
        sys.stdout.write(f"{winner} wins!\n")
    elif is_board_filled(board):
        sys.stdout.write("Draw.\n")


def get_player_input():
    pos = input("Select where you wish to place your character: ")
    return convert_to_tuple(pos)


def convert_to_tuple(input_string):
    remove_space = "".join(input_string.split())
    # validate string (expect 3 chars) eg. "1,2"
    if len(remove_space) != 3 or "," not in remove_space:
        return False
    x, y = remove_space.split(",")
    # verify types
    if not x.isdigit() or not y.isdigit():
        return False
    else:
        x, y = int(x), int(y)
    # validate that arguments are accepted integers from 0-2
    return False if x > 2 or y > 2 or x < 0 or y < 0 else (x, y)


def get_winner(board):
    # predefine all win arrangements
    arrangements = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    # go through each arrangement to find and return the winner
    for win in arrangements:
        x0, y0 = win[0]
        x1, y1 = win[1]
        x2, y2 = win[2]
        if board[x0][y0] == board[x1][y1] == board[x2][y2] and board[x0][y0] != "-":
            return board[x0][y0]
    # check whether board is filled, if there is no winner
    return None


# start the game
start_game()
