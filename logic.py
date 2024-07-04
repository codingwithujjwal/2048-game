import random

def start_game():
    mat = [[0]*4 for _ in range(4)]
    add_new_2(mat)
    add_new_2(mat)
    return mat

def add_new_2(mat):
    r, c = random.choice([(r, c) for r in range(4) for c in range(4) if mat[r][c] == 0])
    mat[r][c] = 2

def move_up(mat):
    # Implement the logic to move up
    return mat, True

def move_down(mat):
    # Implement the logic to move down
    return mat, True

def move_left(mat):
    # Implement the logic to move left
    return mat, True

def move_right(mat):
    # Implement the logic to move right
    return mat, True

def get_current_state(mat):
    # Implement the logic to check the current state
    return 'GAME NOT OVER'
