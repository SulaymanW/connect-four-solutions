import copy
import ConnectFourBoard


# I have tried to improve the MiniMax
# I have not been able to make it work and the AlphaBeta AI is not coded yet


def other(token):
    if token == ConnectFourBoard.RED:
        return ConnectFourBoard.BLUE
    elif token == ConnectFourBoard.BLUE:
        return ConnectFourBoard.RED
    else:
        return None


# estimate of a field quality
def state_score(board, turn):
    (red, blue) = board.score()
    if turn == ConnectFourBoard.RED:
        return red - blue
    else:
        return blue - red


# Comp to play!  Try placing token in each col looking for BIGGEST score
# takes:
#     board: board state
#     token: RED or BLUE
#     ply_remaining: rec. depth
# Returns (col # with MAX score, score)
def max_play(board, token, ply_remaining):
    infinity = float('inf')
    alpha = infinity
    if ply_remaining == 0 or board.is_full():
         return state_score(board, token)

    moves = []
    for col in board.not_full_columns():
        newboard = board.copy()
        if not newboard.attempt_insert(col, token):
            continue
        score = state_score(newboard, token)
        # Got a win! No need to search further, just return this one!
        if score >= board.winscore:
            winning_move = (col, score)
            return winning_move

        else:
            if board.is_full():
                score = state_score(newboard, token)
            else:
                # Sim. human moving, get BEST human move, i.e. col-with-LOWEST-score (or most negative score)
                X = min_play(newboard, other(token), ply_remaining)  # we are the computer
                (min_move, score) = X
            moves.append((col, score))

    # Got all poss. moves
    # return the best one! (col, score)
    best_move = max(moves, key=lambda x: x[1])
    return best_move



# min_play is given other(token)
def min_play(board, token, ply_remaining):
    infinity = float('inf')
    beta = -infinity
    moves = []
    for col in board.not_full_columns():
        newboard = board.copy()
        newboard.attempt_insert(col, token)

        X = max_play(newboard, other(token), ply_remaining-1) # change token back
        score = X if type(X) == int else X[1]
        moves.append((col, score))

    best_move_for_THEM = min(moves, key=lambda x: x[1])
    return best_move_for_THEM


def AIcheck(board, token):
    # Modify to set a different search depth
    ply_remaining = 3
    (move, score) = max_play(board, token, ply_remaining)  # replaced value with score
    return move
