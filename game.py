import board
import ai

# Switches the turn after each move

# Checks if the move is valid
def isValid(user, row, col):
    # Checks first if row or col are out of bounds
    if(row <= -1 or row >= 4 or col <= -1 or col >= 4):
        print("Out of bounds!")
        return False
    if(board.getPiece(row,col) == "O" or board.getPiece(row,col) == "X"): # Checks if occupied already
        print("Invalid move!")
        return False
    else:
        return True



# Checks winner of the game
def check_winner():
    # Player Horizontal
    if(board.getPiece(0,0) == "O" and board.getPiece(0,1) == "O" and board.getPiece(0,2) == "O"):
        return 0
    elif(board.getPiece(1,0) == "O" and board.getPiece(1,1) == "O" and board.getPiece(1,2) == "O"):
        return 0
    elif(board.getPiece(2,0) == "O" and board.getPiece(2,1) == "O" and board.getPiece(2,2) == "O"):
        return 0
    # Player Vertical
    elif(board.getPiece(0,0) == "O" and board.getPiece(1,0) == "O" and board.getPiece(2,0) == "O"):
        return 0
    elif(board.getPiece(0,1) == "O" and board.getPiece(1,1) == "O" and board.getPiece(2,1) == "O"):
        return 0
    elif(board.getPiece(0,2) == "O" and board.getPiece(1,2) == "O" and board.getPiece(2,2) == "O"):
        return 0
    # Player Diagonal
    elif(board.getPiece(0,0) == "O" and board.getPiece(1,1) == "O" and board.getPiece(2,2) == "O"):
        return 0
    elif(board.getPiece(0,2) == "O" and board.getPiece(1,1) == "O" and board.getPiece(2,0) == "O"):
        return 0

    # Ai Horizontal
    elif(board.getPiece(0,0) == "X" and board.getPiece(0,1) == "X" and board.getPiece(0,2) == "X"):
        return 1
    elif(board.getPiece(1,0) == "X" and board.getPiece(1,1) == "X" and board.getPiece(1,2) == "X"):
        return 1
    elif(board.getPiece(2,0) == "X" and board.getPiece(2,1) == "X" and board.getPiece(2,2) == "X"):
        return 1
    # Ai Vertical
    elif(board.getPiece(0,0) == "X" and board.getPiece(1,0) == "X" and board.getPiece(2,0) == "X"):
        return 1
    elif(board.getPiece(0,1) == "X" and board.getPiece(1,1) == "X" and board.getPiece(2,1) == "X"):
        return 1
    elif(board.getPiece(0,2) == "X" and board.getPiece(1,2) == "X" and board.getPiece(2,2) == "X"):
        return 1
    # Ai Diagonal
    elif(board.getPiece(0,0) == "X" and board.getPiece(1,1) == "X" and board.getPiece(2,2) == "X"):
        return 1
    elif(board.getPiece(0,2) == "X" and board.getPiece(1,1) == "X" and board.getPiece(2,0) == "X"):
        return 1
    return -1

# Checks if Draw
def check_draw():
    bFlag = False
    for i in range(3):
        for j in range(3):
            bFlag = board.getPiece(i,j) == " "
            if(bFlag == True):
                return bFlag
    return bFlag

# Displays Winner
def display_winner():
    board.printBoard()
    print("Game over! ", end="")
    if(check_winner() == 1):
        print("Ai wins!")
    else:
        print("Player wins!")
    
# Game Starter
def start_game(user):
    gameOver = False
    while(gameOver == False):
        if(user == 0):
            print("Player 1's turn (O)")
            print("Enter row and col pos : ", end="")
            pos_row, pos_col = [int(x) for x in input().split()] # 2 inputs in one line
            if(isValid(user, pos_row, pos_col)):
                if(winner == -1):
                    board.updateBoard("O", pos_row, pos_col)
                    winner = check_winner()
                    draw = check_draw()
                    if(draw == False):
                        gameOver = True
                        board.printBoard()
                        print("It's a draw!")
                        break
                    user = 1
                elif(winner == 0 or 1):
                    display_winner()
                    gameOver = True
                    break
        else:
            print("AI's turn (X)")
            ai.ai_move()
            winner = check_winner()
            draw = check_draw()
            if(winner == 1):
                display_winner()
                gameOver = True
                break
            elif(draw == False):
                gameOver = True
                print("It's a draw!")
                break
            user = 0 # swaps turn
        board.printBoard()
        print("============================")

