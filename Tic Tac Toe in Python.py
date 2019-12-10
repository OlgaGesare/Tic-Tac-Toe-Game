#Tic Tac Toe Game against a computer, in Python, by Olga Mogaka.

#import
import random

#if game is still in progress
game_in_progress = True
   
#Define the game board.
board = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]

#This function displays the board. 
def display_board():    
    print(board[1],'|',board[2],'|',board[3])
    print('--+---+--')
    print(board[4],'|',board[5],'|',board[6])
    print('--+---+--')
    print(board[7],'|',board[8],'|',board[9])

#Inserts letters to different positions on the board
def insert_board(letter, position):
    #global variable needed
    global board
    board[position] = letter
 
#Checks if a spot on the board has a letter or is free. 
def free_spot(position):
    return board[position] == ' '
    
#Checks if each row, column or diagonal has 3 matching letters (either X or O), which is a win..
def check_win(board, letter):
   
    #row 1
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or 
    #row 2        
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    #row 3
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    #column 1
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    #column 2
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    #column 3
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    #diagonal 1
    (board[7] == letter and board[5] == letter and board[3] == letter) or
    #diagonal 2
    (board[9] == letter and board[5] == letter and board[1] == letter))
    return

#check if there is a tie
def check_tie():
  global game_in_progress
  if "-" not in board:
    game_in_progress = False
  return

  main()

#Function to guide player on free spaces and those occupied
def play():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' from 1 to 9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free_spot(move):
                    run = False
                    insert_board('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number from 1 to 9: ')
        except:
            print('Invalid input. Please type a number!')
       
#Randomly selects a space for the computer 
def random_select(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
   
#Computer checks for possible winning move or to block opponent's winning move 
def comp_move():
    possible_moves = [X for X, letter in enumerate(board) if letter == ' ' and X != 0]
    move = 0
   
    for let in ['O','X']:
        for i in possible_moves:
            copy_board = board[:]
            copy_board[i] = let
            if check_win(copy_board, let):
                move = i
                return move
 
    #Try to take one of the corners if available
    corners_available = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners_available.append(i)
    if len(corners_available) > 0:
        move = random_select(corners_available)
        return move
   
    #Try to take the center if available
    if 5 in possible_moves:
        move = 5
        return move
 
    #Take any edge if available
    edges_available = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            edges_available.append(i)
 
    if len(edges_available) > 0:
        move = random_select(edges_available)
 
    return move
 
#Check to see if there are available spaces
def board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
 
#Main game loop
def main():

    print('Welcome to the TIC TAC TOE GAME, to win complete a straight line of your letter (column, row or diagonal) and select positions 1-9 starting at the top left.')
    display_board()
 
    while not(board_full(board)):
        if not(check_win(board, 'O')):
            play()
            display_board()
        else:
            print('Computer wins!')
            break
       
        if not(check_win(board, 'X')):
            move = comp_move()
            if move == 0:
                print('Game is a Tie!')
            else:
                insert_board('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                display_board()
        else:
            print('Human wins!')
            break

main()

#Restart the game
while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('..........................')
        main()
    else:
        break
