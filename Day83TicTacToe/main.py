# Tic Tac Toe Game in Python

# Function to print the game board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


# Function to check if someone has won
def check_win(board, mark):
    # Check rows, columns, and diagonals for a win
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals
    return any(board[a] == board[b] == board[c] == mark for a, b, c in win_conditions)


# Function to check if the board is full (draw)
def check_draw(board):
    return " " not in board


# Function to handle a player's move
def player_move(board, mark):
    while True:
        try:
            position = int(input(f"Player {mark}, choose your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid input! Please choose a number between 1 and 9.")
            elif board[position] != " ":
                print("This position is already taken. Choose another.")
            else:
                board[position] = mark
                break
        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to switch between players
def switch_player(current_player):
    return "O" if current_player == "X" else "X"


# Main function to run the Tic Tac Toe game
def play_game():
    print("Welcome to Tic Tac Toe!")

    # Initialize an empty game board
    board = [" " for _ in range(9)]

    # Starting player
    current_player = "X"

    # Main game loop
    while True:
        # Print the current state of the board
        print_board(board)

        # Handle player's move
        player_move(board, current_player)

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = switch_player(current_player)


# Start the game
if __name__ == "__main__":
    play_game()
