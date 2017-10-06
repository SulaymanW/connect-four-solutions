import copy
import ConnectFourBoard
import random


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


def max_play(board, token, ply_remaining):
    moves = []

    for col in board.not_full_columns():
        newboard = board.copy()
        newboard.attempt_insert(col, token)
    if ply_remaining <= 0 or newboard.is_full():
        value = state_score(newboard, token)
    else:
        (min_move, value) = min_play(newboard, token, ply_remaining-1)
    moves.append((col, value))
    random.shuffle(moves)
    move = max(moves, key=lambda x: x[1])
    return move


def min_play(board, token, ply_remaining):
    # Initially empty set of possible moves
    moves = []
    # Loop over columns that still have space
    for col in board.not_full_columns():
        # Copy the game state so the AI can mess with it
        newboard = board.copy()
        # Insert a new token of the opponent's colour
        newboard.attempt_insert(col, other(token))
        # compute the new board value
        value = state_score(newboard, token)
        # Add the info to the list of moves
        moves.append((col, value))
    # Select the worst move
    worst_move = min(moves, key=lambda x: x[1])
    return worst_move


def AIcheck(board, token):
    # Modify to set a different search depth
    ply_remaining = 3
    (move, value) = max_play(board, token, ply_remaining)
    return move

