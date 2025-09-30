def winner(board):
    for i in range(3):
        if board[i][0] != '.' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != '.' and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] != '.' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != '.' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def empty_cells(board):
    return [(i,j) for i in range(3) for j in range(3) if board[i][j]=='.']

def minimax(board, is_max, player, opponent):
    win = winner(board)
    if win == player: return 10
    if win == opponent: return -10
    if not empty_cells(board): return 0
    
    if is_max:
        best = -999
        for i,j in empty_cells(board):
            board[i][j] = player
            best = max(best, minimax(board, False, player, opponent))
            board[i][j] = '.'
        return best
    else:
        best = 999
        for i,j in empty_cells(board):
            board[i][j] = opponent
            best = min(best, minimax(board, True, player, opponent))
            board[i][j] = '.'
        return best

def best_move(board, turn):
    opponent = 'O' if turn=='X' else 'X'
    best_val = -999
    move = None
    for i,j in empty_cells(board):
        board[i][j] = turn
        score = minimax(board, False, turn, opponent)
        board[i][j] = '.'
        if score > best_val:
            best_val = score
            move = (i,j)
    return move, best_val

# Interactive Part
print("\n\nEnter the Tic-Tac-Toe board (3 rows, use X, O, . for empty):")
board = [list(input().strip().upper()) for _ in range(3)]
turn = input("Enter the current player (X or O): ").strip().upper()

move, score = best_move(board, turn)
if move:
    print(f"Optimal move for {turn}: Row {move[0]+1}, Col {move[1]+1}")
    if score > 0: print(f"Predicted result: {turn} will win")
    elif score < 0: print("Predicted result: Opponent will win")
    else: print("Predicted result: Draw")
else:
    print("No moves left. Game over.")
