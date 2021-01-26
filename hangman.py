# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 22:19:46 2019

@author: Eric
"""

import random


def check_correct(word, user_inp):
    
    pos = []
    
    for i, letter in enumerate(word):
        if letter == user_inp:
            pos.append(i)
            
    if len(pos) > 0:
        return True, pos
    else:
        return False, pos
    
    
    
def draw_game(board, game_letters, wrong_letters):
    
    for row in board:
        line = ''
        for ele in row:
            line = line + ele
        print(line)
        
    print()
    
    line = ''
    for letter in game_letters:
        line = line + letter + ' '
        
    print(line)
    
    print()
    
    line = 'wrong letters: '
    for letter in wrong_letters:
        line = line + letter + ' '
        
    print(line)
    
        
    
def main():
    
    word_array = ['ham', 'carrot', 'bicycle', 'airplane', 'mississippi', 
                  'computer', 'sheets', 'map', 'island', 'syrup', 'fridge',
                  'soccer', 'controller', 'wire', 'mouse', 'cardboard', 'bowl',
                  'dresser', 'container', 'drums', 'trash', 'notebook']
    
    terminate = False
    
    while not terminate:
    
        num = random.randint(0, (len(word_array) - 1))
        
        selected_word = word_array[num]
        
        word = []
                
        for letter in selected_word:
            word.append(letter)
            
        r1 = [' ', '_', '_', '_', '_', '_', ' ']
        r2 = [' ', '|', ' ', ' ', ' ', '|', ' ']
        r3 = [' ', '|', ' ', ' ', ' ', ' ', ' ']
        r4 = [' ', '|', ' ', ' ', ' ', ' ', ' ']
        r5 = [' ', '|', ' ', ' ', ' ', ' ', ' ']
        r6 = [' ', '|', ' ', ' ', ' ', ' ', ' ']
        r7 = ['-', '-', '-', '-', ' ', ' ', ' ']
        
        board = [r1, r2, r3, r4, r5, r6, r7]
        
        game_letters = []
        
        for letter in word:
            game_letters.append('_ ')
        
        
        
        print()
        print('type "quit" to quit')
        print('start guessing!!!')
        
        wrong_count = 0
        used_letters = []
        wrong_letters = []
        terminate2 = False
        
        while not terminate2:
            
            draw_game(board, game_letters, wrong_letters)
            
            valid_input = False
            while not valid_input:
            
                user_inp = input('>  ')
                
                if user_inp == 'quit':
                    
                    print()
                    print('Thanks for playing')
                    valid_input = True
                    terminate = True
                    terminate2 = True
                
                elif len(user_inp) == 1 and user_inp.isalpha():
                    
                    user_inp = user_inp.lower()
                    if user_inp not in used_letters:
                        
                        valid_input = True
                        
                    else:
                        print('letter already used')
                
                else:
                    print('invalid input')
                    print()
                    
            correct, pos = check_correct(word, user_inp)
            
            
            if correct:
                
                for ele in pos:
                    game_letters[ele] = word[ele] + ' '
                    used_letters.append(user_inp)
                    
                if '_ ' not in game_letters:
                    draw_game(board, game_letters, wrong_letters)
                    print()
                    print('YOU WIN')
                    terminate2 = True
                
            else:
                
                used_letters.append(user_inp)
                wrong_letters.append(user_inp)
                
                wrong_count += 1
                    
                if wrong_count >= 6:
                    (board[5])[6] = '\\'
                    draw_game(board, game_letters, wrong_letters)
                    print()
                    print('YOU LOSE')
                    print('the word was: ' + selected_word)
                    terminate2 = True
                elif wrong_count == 5:
                    (board[5])[4] = '/'
                elif wrong_count == 4:
                    (board[3])[6] = '\\'
                elif wrong_count == 3:
                    (board[3])[4] = '/'
                elif wrong_count == 2:
                    (board[3])[5] = '|'
                    (board[4])[5] = '|'
                elif wrong_count == 1:
                    (board[2])[5] = 'O'
                
            
        if not terminate:
        
            print()
            print('Would you like to play again? (y/n)')
            
            valid_input = False
            while not valid_input:
                user_inp = input('>  ')
                
                if user_inp.isalpha():
                    user_inp = user_inp.lower()
                    
                    if user_inp == 'y':
                        valid_input = True
                    elif user_inp == 'n':
                        print()
                        print('Thanks for playing')
                        valid_input = True
                        terminate = True
                    else:
                        print('invalid input')
                else:
                    print('invalid input')
    
    
    
if __name__ == "__main__":
    main()