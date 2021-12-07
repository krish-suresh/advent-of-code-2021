import numpy as np
lines = []
with open('day_4/bingo.txt') as f:
    lines = f.readlines()
def chunk_string(str, n = 3):
    return [str[i:i+n] for i in range(0, len(str), n)]
def has_win(board_bin):
    for row in board_bin:
        if np.all((row == 0)):
            return True
    for col in np.transpose(board_bin):
        if np.all((col == 0)):
            return True
    return False

bingo_numbers = [int(x.strip()) for x in lines[0].split(',')]
board_num = 0 
boards = []
boards.append([])
line_num = 0
for line in lines[2:]:
    if line == "\n":
        board_num += 1
        line_num = 0
        boards.append([])
    else:
        boards[board_num].append([int(x.strip()) for x in chunk_string(line)])
        line_num += 1
boards = np.array(boards)
boards_binary = np.ones(boards.shape)
output = 0
won_boards = np.full(boards.shape[0], False)
for i, num in enumerate(bingo_numbers):
    for j, board in enumerate(boards):
        ind = np.where(board == num)
        board[ind] = 0
        if not won_boards[j] and has_win(board):
            output = int(np.sum(board))*num
            won_boards[j] = True
print(output)