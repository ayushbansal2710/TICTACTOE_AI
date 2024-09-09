import random

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)               # Diagonals
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    if EMPTY not in board:
        return 'Draw'
    return None

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]

def make_move(board, move, player):
    board[move] = player

def undo_move(board, move):
    board[move] = EMPTY

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    if winner == PLAYER_X:
        return 10 - depth
    if winner == PLAYER_O:
        return depth - 10
    if winner == 'Draw':
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for move in available_moves(board):
            make_move(board, move, PLAYER_X)
            score = minimax(board, depth + 1, False)
            undo_move(board, move)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in available_moves(board):
            make_move(board, move, PLAYER_O)
            score = minimax(board, depth + 1, True)
            undo_move(board, move)
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for move in available_moves(board):
        make_move(board, move, PLAYER_X)
        score = minimax(board, 0, False)
        undo_move(board, move)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = [EMPTY] * 9
    print_board(board)
    
    while True:
        # Player move
        try:
            player_move = int(input("Enter your move (0-8): "))
            if board[player_move] == EMPTY:
                make_move(board, player_move, PLAYER_O)
            else:
                print("Invalid move. Try again.")
                continue
        except (IndexError, ValueError):
            print("Invalid input. Enter a number between 0 and 8.")
            continue
        
        if check_winner(board):
            print_board(board)
            print("You win!")
            break
        elif EMPTY not in board:
            print_board(board)
            print("It's a draw!")
            break
        
        # AI move
        ai_move = find_best_move(board)
        make_move(board, ai_move, PLAYER_X)
        print(f"AI plays {ai_move}")
        
        if check_winner(board):
            print_board(board)
            print("AI wins!")
            break
        elif EMPTY not in board:
            print_board(board)
            print("It's a draw!")
            break

        print_board(board)
    
    print("Game over! Thanks for playing.")

if __name__ == "__main__":
    play_game()
