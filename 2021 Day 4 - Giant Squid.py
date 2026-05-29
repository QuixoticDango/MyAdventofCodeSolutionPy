import types
def is_winner(board: list[list[int]]):
    # print(f"{marked = }")
    for row in board:
        if all(ch in marked for ch in row):
            print(f"ROW RETURN")
            print(f"{row = }")
            return row
    for col in zip(*board):
        if all(ch in marked for ch in col):
            print(f"COLUMN RETURN")
            print(f"{col = }")
            return col
    return None

def product(*args) -> int:
    p = 1
    for i in args:
        p *= i
    return p

# def mark_boards(board, num):
#     for i, row in enumerate(board):
#         for j, space in enumerate(row):
#             if space == num:
#                 board[i][j] = '*'

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 4 Advent of Code Input.txt"

with open(file) as f:
    draws = tuple(f.readline().strip().split(','))
    # print(f"{draws = }")
    _ = f.readline()
    boards = []
    board = []
    for line in f.readlines():
        if line == '\n':
            boards.append(board)
            board = []
            continue
        board.append(line.strip().split())
    else:
        boards.append(board)

marked = set()
winner = None
score = None
for draw in draws:
    marked.add(draw)
    if winner:
        break
    for board in boards:
        winner = is_winner(board)
        if winner:
            score = sum(int(mark) for row in board for mark in row if mark not in marked) * int(draw)
            break
# print(f"{marked=}")
print(f"Part 1: {score}")

marked = []
completed_boards = []
last_board = None
for draw in draws:
    if len(boards) == len(completed_boards):
        break
    marked.append(draw)
    for board in boards:
        if board not in completed_boards:
            if is_winner(board):
                completed_boards.append(board)
last_board = completed_boards[-1]
score = sum(int(mark) for row in last_board for mark in row if mark not in marked) * int(marked[-1])
print(f"Part 2: {score}")