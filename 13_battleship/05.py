board = []
for i in range(5):
    board.append(["O"] * 5)

# or
# board = [["O"] * 5] * 5

def print_board(board):
    for row in board:
        print row

print_board(board)
