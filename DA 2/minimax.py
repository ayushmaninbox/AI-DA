def minimax(values, depth, index, is_max, max_depth):
    if depth == max_depth:
        return values[index]
    if is_max:
        return max(
            minimax(values, depth+1, index*2, False, max_depth),
            minimax(values, depth+1, index*2+1, False, max_depth)
        )
    else:
        return min(
            minimax(values, depth+1, index*2, True, max_depth),
            minimax(values, depth+1, index*2+1, True, max_depth)
        )

def alpha_beta(values, depth, index, is_max, max_depth, alpha, beta):
    if depth == max_depth:
        return values[index]
    if is_max:
        best = -999
        for i in range(2):
            val = alpha_beta(values, depth+1, index*2+i, False, max_depth, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    else:
        best = 999
        for i in range(2):
            val = alpha_beta(values, depth+1, index*2+i, True, max_depth, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha: break
        return best

print("\n\nEnter 8 leaf node values (space separated):")
leaf_nodes = list(map(int, input().split()))
if len(leaf_nodes) != 8:
    print("You must enter exactly 8 values. Exiting.")
else:
    max_depth = 3
    print("Minimax result:", minimax(leaf_nodes, 0, 0, True, max_depth))
    print("Alpha-Beta result:", alpha_beta(leaf_nodes, 0, 0, True, max_depth, -999, 999))
