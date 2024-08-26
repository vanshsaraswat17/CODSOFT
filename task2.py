import math

print('''
      

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
''')


def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")

def check_winner(board):
    # Possible winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != '-':
            return board[combo[0]]
    
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif '-' not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = '-'
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = '-'
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == '-':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = '-'
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = ['-'] * 9
    player = input("Do you want to be X or O? ").upper()
    ai = 'O' if player == 'X' else 'X'
    
    while True:
        print_board(board)
        if '-' not in board:
            print("It's a draw!")
            break
        
        # Human move
        human_move = int(input(f"Enter your move (1-9) as {player}: ")) - 1
        if board[human_move] != '-':
            print("Invalid move. Try again.")
            continue
        board[human_move] = player

        if check_winner(board):
            print_board(board)
            print(f"{player} wins!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = ai

        if check_winner(board):
            print_board(board)
            print(f"{ai} wins!")
            break

# Start the game
play_game()

