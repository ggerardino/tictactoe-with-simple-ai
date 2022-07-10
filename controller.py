import board
import ai

# Switches the turn after each move

# Checks if the move is valid
def isValid(turn, row, col):
    # Checks first if row or col are out of bounds
    if(row <= -1 or row >= 4 or col <= -1 or col >= 4):
        print("Out of bounds!")
        return False
    if(turn == 0):
        if(board.getPiece(row,col) == "O" or board.getPiece(row,col) == "X"): # Checks if occupied already
            print("Invalid move!")
            return False
        else:
            return True
    elif(turn == 1):
        return True

# Checks winner of the game
def check_winner(turn):
    if(turn == 1):
        mark = "X"
    else:
        mark = "O"
    # Player Horizontal
    if(    (board.getPiece(0,0) == board.getPiece(0,1) == board.getPiece(0,2) == mark) 
        or (board.getPiece(1,0) == board.getPiece(1,1) == board.getPiece(1,2) == mark)
        or (board.getPiece(1,0) == board.getPiece(1,1) == board.getPiece(1,2) == mark)
        or (board.getPiece(0,0) == board.getPiece(1,0) == board.getPiece(2,0) == mark)
        or (board.getPiece(0,1) == board.getPiece(1,1) == board.getPiece(2,1) == mark)
        or (board.getPiece(0,2) == board.getPiece(1,2) == board.getPiece(2,2) == mark)
        or (board.getPiece(0,0) == board.getPiece(1,1) == board.getPiece(2,2) == mark)
        or (board.getPiece(0,2) == board.getPiece(1,1) == board.getPiece(2,0) == mark)):
        if(turn == 1):
            return 1 # if Ai wins
        else:
            return 0 # if Player wins
    return -1

# Checks if Draw
def check_draw():
    for i in range(3):
        for j in range(3):
            if(board.getPiece(i,j) == " "):
              return True
    return False

# Displays Winner
def display_winner(turn):
    board.printBoard()
    print("Game over! ", end="")
    if(turn == 1):
        print("Ai wins!")
    else:
        print("Player wins!")
    
# Game Starter // used before implementing gui 
def start_game(turn):
    gameOver = False
    while(gameOver == False):
        if(turn == 0):
            print("Player 1's turn (O)")
            print("Enter row and col pos : ", end="")
            pos_row, pos_col = [int(x) for x in input().split()] # 2 inputs in one line
            if(isValid(turn, pos_row, pos_col)):
                if(winner == -1):
                    board.updateBoard("O", pos_row, pos_col)
                    winner = check_winner(turn)
                    draw = check_draw()
                    if(draw == False):
                        gameOver = True
                        board.printBoard()
                        print("It's a draw!")
                        break
                    turn = 1
                elif(winner == 0 or 1):
                    display_winner(turn)
                    gameOver = True
                    break
        else:
            print("AI's turn (X)")
            ai.ai_move(turn)
            winner = check_winner(turn)
            draw = check_draw()
            if(winner == 1):
                display_winner(turn)
                gameOver = True
                break
            elif(draw == False):
                gameOver = True
                print("It's a draw!")
                break
            turn = 0 # swaps turn
        board.printBoard()
        print("============================")

