import random

# Function to print the game board
def print_board(board, dimension):
    count = dimension * dimension
    for row in board:
        print(" | ".join(row))
        print("-" * count)

# Function to check if a player has won
def check_win(board, player, dimension):
    for i in range(dimension):
        if all([board[i][j] == player for j in range(dimension)]) or all([board[j][i] == player for j in range(dimension)]):
            return True
    if all([board[i][i] == player for i in range(dimension)]) or all([board[i][2-i] == player for i in range(dimension)]):
        return True
    return False

# Function to check if the game is a tie
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to get the player's move
def get_player_move(board: str, player: str, dimension: int):
    count = dimension * dimension
    while True:
        try:
            player_input = input(f"Player {player}, enter your move (1-{count}): ")
            if player_input == 'exit':
                break
                
            
            move = int(input(f"Player {player}, enter your move (1-{count}): "))
            if move < 1 or move > count:
                raise ValueError
            row = (move - 1) // dimension
            col = (move - 1) % dimension
            if board[row][col] != " ":
                raise ValueError
            return row, col
        except ValueError:
            print(f"Invalid move. Please choose an empty cell (1-{count}).")

# Function for the computer's move
def get_computer_move(board, dimension):
    while True:
        row = random.randint(0, dimension-1)
        col = random.randint(0, dimension-1)
        if board[row][col] == " ":
            return row, col

# Function to start a new game
def start_game(dimension: int, vals: list):
    """
    
    """
    
    # generate string of vals with 'or' connection
    val_prompt = ''
    for i in range(len(vals)):
        if i == len(vals) -1:
            val_prompt  = val_prompt + ' ' + vals[i]
        else:
            val_prompt = val_prompt + ' ' + vals[i] + ' or'
    
    
    board = [[" " for _ in range(dimension)] for _ in range(dimension)]
    print(board)
    print("Welcome to Tic-Tac-Toe!")
    print("Your opponent is a computer,enter exit if you want to terminate the game.")
    player = input(f'Choose {val_prompt}: ').upper()

    if player == 'EXIT':
        print('quit game...')
        return

    while player not in vals:
        print(f'Invalid choice. Please choose {val_prompt}.')
        player = input(f'Choose {val_prompt}: ').upper()
    
    if player == vals[0]:
        computer = vals[1]
    else:
        computer = vals[0]
    
    print("You chose", player)
    print("Computer plays", computer)
    print_board(board, dimension)
    
    while True:
        row, col = get_player_move(board, player, dimension)
        if [row, col] == [-1, -1]:
            print('quit game...')
            break

        board[row][col] = player
        print_board(board, dimension)
        if check_win(board, player, dimension):
            print("Player", player, "wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

        row, col = get_computer_move(board, dimension)
        board[row][col] = computer
        print("Computer plays at cell", (row * dimension) + col + 1)
        print_board(board, dimension)
        if check_win(board, computer, dimension):
            print("Player", computer, "wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

# Start the game

dimension = 3
vals = ["X", "O"]
start_game(dimension, vals)
