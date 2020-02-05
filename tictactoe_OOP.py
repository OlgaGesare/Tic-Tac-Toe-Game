#Tic Tac Toe Game against a computer, in Python, by Olga Mogaka.

import random
import os
os.system('clear')


class Board():
    def __init__(self):
        self.board =  [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]

    def display(self):
        print(self.board[1],'|',self.board[2],'|',self.board[3])
        print('--+---+--')
        print(self.board[4],'|',self.board[5],'|',self.board[6])
        print('--+---+--')
        print(self.board[7],'|',self.board[8],'|',self.board[9])        

    def update_board(self, board_no, letter):
        if self.board[board_no] == ' ':
            self.board[board_no] = letter
        else:
            return False
              

    def is_winner(self, letter):
        if self.board[1] == letter and self.board[2] == letter and self.board[3]== letter:
            return True  
        if self.board[4] == letter and self.board[5] == letter and self.board[6]== letter:
            return True
        if self.board[7] == letter and self.board[8] == letter and self.board[9]== letter:
            return True
        if self.board[1] == letter and self.board[4] == letter and self.board[7]== letter:
            return True
        if self.board[2] == letter and self.board[5] == letter and self.board[8]== letter:
            return True
        if self.board[3] == letter and self.board[6] == letter and self.board[9]== letter:
            return True
        if self.board[1] == letter and self.board[5] == letter and self.board[9]== letter:
            return True
        if self.board[3] == letter and self.board[5] == letter and self.board[7]== letter:
            return True

        return False

    def is_tie(self):
        used_board = 0
        for board in self.board:
            if board != ' ':
                used_board +=1
        if used_board == 9:
            return True
        else:
            return False

    def reset(self):
        self.board = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]


    def defend(self, letter):
        if self.board[1] == 'X' and self.board[2] == 'X' and self.board[3] == ' ':
            self.update_board(3, letter)
            return True
        if self.board[1] == 'X' and self.board[3] == 'X' and self.board[2] == ' ':
            self.update_board(2, letter)
            return True
        if self.board[2] == 'X' and self.board[3] == 'X' and self.board[1] == ' ':
            self.update_board(1, letter)
            return True
        if self.board[4] == 'X' and self.board[5] == 'X' and self.board[6] == ' ':
            self.update_board(6, letter)
            return True
        if self.board[5] == 'X' and self.board[6] == 'X' and self.board[4] == ' ':
            self.update_board(4, letter)
            return True
        if self.board[4] == 'X' and self.board[6] == 'X' and self.board[5] == ' ':
            self.update_board(5, letter)
            return True
        if self.board[7] == 'X' and self.board[8] == 'X' and self.board[9] == ' ':
            self.update_board(9, letter)
            return True
        if self.board[8] == 'X' and self.board[9] == 'X' and self.board[3] == ' ':
            self.update_board(7, letter)
            return True
        if self.board[7] == 'X' and self.board[9] == 'X' and self.board[8] == ' ':
            self.update_board(8, letter)
            return True
        if self.board[2] == 'X' and self.board[8] == 'X' and self.board[5] == ' ':
            self.update_board(5, letter)
            return True
        if self.board[5] == 'X' and self.board[8] == 'X' and self.board[2] == ' ':
            self.update_board(2, letter)
            return True
        if self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == ' ':
            self.update_board(8, letter)
            return True
        if self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == ' ':
            self.update_board(7, letter)
            return True
        if self.board[4] == 'X' and self.board[7] == 'X' and self.board[1] == ' ':
            self.update_board(1, letter)
            return True
        if self.board[1] == 'X' and self.board[7] == 'X' and self.board[4] == ' ':
            self.update_board(4, letter)
            return True
        if self.board[3] == 'X' and self.board[6] == 'X' and self.board[9] == ' ':
            self.update_board(9, letter)
            return True
        if self.board[6] == 'X' and self.board[9] == 'X' and self.board[3] == ' ': 
            self.update_board(3, letter)
            return True
        if self.board[3] == 'X' and self.board[9] == 'X' and self.board[6] == ' ':
            self.update_board(6, letter)
            return True        
        
    def ai_move(self, letter):
        possible_moves = [X for X, letter in enumerate(self.board) if letter == ' ' and X != 0]
        move = 0


        if self.board[5] == ' ':
            self.update_board(5, letter)
            return True
        
            self.defend(letter)
            return True


        corners_available = []
        for i in possible_moves:
            if i in [1,3,7,9]:
                corners_available.append(i)
        if len(corners_available) > 0:
            move = random_select(corners_available)
            self.update_board(move, letter)
            return True


        edges_available = []
        for i in possible_moves:
            if i in [2,4,6,8]:
                edges_available.append(i)
        if len(edges_available) > 0:
            move = random_select(edges_available)
            self.update_board(move, letter)
            return True               
        

board = Board()

    
def random_select(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def print_header():
    print('Welcome to the Tic-Tac_Toe game')

def refresh_screen():
    os.system('clear')

    print_header()

    board.display()
    

while True:    
    refresh_screen()

    run = True
    while run:
        try:
            x_choice = int(input('\nX) Please choose 1 - 9, > '))
            if x_choice >0 and x_choice < 10:
                run = False

            else:
                print('Please type a number from 1 to 9: ')
        
        except:
            print('Invalid input. Please type a number!')

    while board.update_board(x_choice,'X') == False:
        print('Position taken, please choose another one')
        x_choice = int(input('\nX) Please choose 1-9 > '))
        

    board.update_board(x_choice, 'X')

    refresh_screen()

    if board.is_winner('X'):
        print('\nX wins!\n')
        play_again = input('Would you like to play again? (Y/N) > ').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print('\n Tie game!\n')
        play_again = input('Would you like to play again? (Y/N) > ').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break


    board.ai_move('O')

    refresh_screen()

        
    if board.is_winner('O'):
        print('\nO wins!\n')
        play_again = input('Would you like to play again? (Y/N) > ').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break 

    if board.is_tie():
        print('\n Tie game!\n')
        play_again = input('Would you like to play again? (Y/N) > ').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break
