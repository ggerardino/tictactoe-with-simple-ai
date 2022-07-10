import board
import controller
import math

def ai_move(turn):
    bestScore = -math.inf
    bestMove = [0,0]
    for i in range(3):
        for j in range(3):
            if(board.getPiece(i, j) == " "):
                board.updateBoard("X", i, j)
                score = minimax(turn, board, 0, False)
                board.updateBoard(" ", i, j)
                if(score > bestScore):
                    bestScore = score
                    bestMove = [i, j]
    board.updateBoard("X", bestMove[0], bestMove[1])

def minimax(turn, board, depth, isMaximizing):
    if(controller.check_winner(turn) == 1):
        return 1
    elif(controller.check_winner(turn) == 0):
        return -1
    elif(controller.check_draw() == False):
        return 0
    
    if(isMaximizing == True):
        bestScore = -math.inf
        for i in range(3):
            for j in range(3):
                if(board.getPiece(i, j) == " "):
                    board.updateBoard("X", i, j)
                    score = minimax(turn, board, depth + 1, False)
                    board.updateBoard(" ", i, j)
                    if(score > bestScore):
                        bestScore = score
        return bestScore
    else:
        bestScore = math.inf
        for i in range(3):
            for j in range(3):
                if(board.getPiece(i, j) == " "):
                    board.updateBoard("O", i, j)
                    score = minimax(turn, board, depth + 1, True)
                    board.updateBoard(" ", i, j)
                    if(score < bestScore):
                        bestScore = score
        return bestScore
                    

