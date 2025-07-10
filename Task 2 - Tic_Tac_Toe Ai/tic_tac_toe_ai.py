#TIC_TAC_TOE_AI USING MINIMAX

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
    print()

# Check for winner or draw
def check_winner():
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

# Human move
def player_move():
    while True:
        try:
            pos = int(input("Enter position (0-8): "))
            if board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("That spot is taken.")
        except (ValueError, IndexError):
            print("Invalid input. Enter number between 0 and 8.")

# AI move using Minimax
def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Minimax algorithm
def minimax(is_maximizing):
    result = check_winner()
    if result == "X":
        return -1
    elif result == "O":
        return 1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Game loop
def play_game():
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board()
    while True:
        player_move()
        print_board()
        if check_winner():
            break
        ai_move()
        print("AI's move:")
        print_board()
        if check_winner():
            break

    result = check_winner()
    if result == "Draw":
        print("It's a Draw!")
    else:
        print(f"{result} wins!")

# Run the game
play_game()