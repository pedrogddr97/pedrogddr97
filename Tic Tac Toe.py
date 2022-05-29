# Code for a tic tac toe game in the terminal
# Variables
from turtle import clear
clear

import random
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None # At the beginning there is no winner
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | "  + board[2] + " | " )
    print("-----------")
    print(board[3] + " | " + board[4] + " | "  + board[5] + " | " )
    print("-----------")
    print(board[6] + " | " + board[7] + " | "  + board[8] + " | " )
    print("-----------")



# Take player input
def playerInput(board):
    inp = int(input("Enter a number 1 - 9:")) # Pedimos un numero entero
    if inp >= 1 and inp <= 9 and board[inp-1 == "-"]: # Check that the player input is valid and unoccupied
        board[inp-1] = currentPlayer # We set that the position equal to the current player
    else:
        print("Oops! Invalid selection, spot is occupied or invalid. Please select a valid input")



# Check for win, lose, or tie outcome
# Check for horizontal win
def checkHorizontal(board):
    global winner # Global means that if this specific scenario is fulfilled, the variable changes throughout the entire code
    if board[0] == board[1] == board[2] and board[1] != "-": # If the horizonatl line is the same and there is no dash ("-"), the player wins
        winner = board[0] # Does not matter which bracket as they are all equal
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# Check for collumn win
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# Check for diagonal win
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[0] != "-":
        winner = board[2]
        return True


# Check for any tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

# Check for win
def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")
        gameRunning = False



# Switch the player (or AI)
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Create AI
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()



# Check again for win, lose, or tie outcome

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)



