# Original files

import copy
import ConnectFourBoard


def other(token):
    if token == ConnectFourBoard.RED:
        return ConnectFourBoard.BLUE
    elif token == ConnectFourBoard.BLUE:
        return ConnectFourBoard.RED
    else:
        return None


# estimate of a field quality
def state_score(game, field):
    # TODO: complete this function
    return 0

def max_play(board, token, ply_remaining):
    # TODO: implement Max playing
    return None
def min_play(board, token, ply_remaining):
    return token
def AIcheck(board, token):
    # Modify to set a different search depth
    ply_remaining = 3
    (move, value) = max_play(board, token, ply_remaining)
    return move

