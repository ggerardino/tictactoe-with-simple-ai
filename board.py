board = [   [" "," "," "],
            [" "," "," "],
            [" "," "," "]  ]

# Displays the board
def printBoard():
    for i in range(3):
        for j in range(3):
            if(board[i][j] == " "):
                print("[ ]", end="")
            else:
                print("[" + board[i][j] + "]", end="")
        print("")

# Updates the board after move 
def updateBoard(mark, row, col):
    board[row][col] = mark

# Returns the value of its index given the row and col
def getPiece(row, col):
    return board[row][col]
