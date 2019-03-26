# Tic Tac Toe

import random

# This function prints out the board that it was passed.
def DrawBoard(board):
    
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# This function lets the player choose which the letter they want to be.
def InputPlayerLetter():
    
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

# This function randomly chooses who goes first.
def FirstPlayer():
    
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

# This function returns True if the player wants to play again, otherwise it returns False.
def PlayAgain():
    
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def MakeMove(board, letter, move):
    board[move] = letter

# Given a board and a player's letter, this function returns True if that player has won.
def IsWinner(bo, le):
    
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

# This function makes a duplicate of the board list and returns the duplicate.
def GetBoardCopy(board):
    
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

# This function returns true if the passed move is free on the passed board.
def IsSpaceFree(board, move):
    
    return board[move] == ' '

# This function lets the player type in his move.
def GetPlayerMove(board):
    
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not IsSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

# Returns a valid move from the passed list on the passed board.
# Returns None if there is no valid move.
def ChooseRandomMoveFromList(board, movesList):
    
    PossibleMoves = []
    for i in movesList:
        if IsSpaceFree(board, i):
            PossibleMoves.append(i)

    if len(PossibleMoves) != 0:
        return random.choice(PossibleMoves)
    else:
        return None

# Given a board and the computer's letter, determine where to move and return that move.
def GetComputerMove(board, ComputerLetter):
    
    if ComputerLetter == 'X':
        PlayerLetter = 'O'
    else:
        PlayerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # Check if we can win in the next move
    for i in range(1, 10):
        copy = GetBoardCopy(board)
        if IsSpaceFree(copy, i):
            MakeMove(copy, ComputerLetter, i)
            if IsWinner(copy, ComputerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = GetBoardCopy(board)
        if IsSpaceFree(copy, i):
            MakeMove(copy, PlayerLetter, i)
            if IsWinner(copy, PlayerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = ChooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if IsSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return ChooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if IsSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    PlayerLetter, ComputerLetter = InputPlayerLetter()
    turn = FirstPlayer()
    print('The ' + turn + ' will go first.')
    GameIsPlaying = True

    while GameIsPlaying:
        if turn == 'player':
            # Player's turn.
            DrawBoard(theBoard)
            move = GetPlayerMove(theBoard)
            MakeMove(theBoard, PlayerLetter, move)

            if IsWinner(theBoard, PlayerLetter):
                DrawBoard(theBoard)
                print('Hooray! You have won the game!')
                GameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    DrawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = GetComputerMove(theBoard, ComputerLetter)
            MakeMove(theBoard, ComputerLetter, move)

            if IsWinner(theBoard, ComputerLetter):
                DrawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                GameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    DrawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not PlayAgain():
        break
