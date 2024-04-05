import random
import time

def print_board(board, streak):
    
    for ele in board:
        line = ''
        for item in ele:
            line = line + ' ' + item
        print(line)
            
    print('STREAK: ' + str(streak))
    
def death(board):
    print('        ___             ___       ___   ___')
    print(' \\   / /   \\ |   |     |   \\  |  |     |   \\')
    print('  \\ /  |   | |   |     |   |  |  |__   |   |')
    print('   |   |   | |   |     |   |  |  |     |   |')
    print('   |   \\___/ \\___/     |___/  |  |___  |___/')
    print()
    
    
    (board[-3])[2] = '^'
    
    
    player = [2, 2]
    
    streak = 0
    
    return board, player, streak
    
def win():
    print()
    print('        ___                                ')
    print(' \\   / /   \\ |   |      |        | | |\\   |')
    print('  \\ /  |   | |   |      |        | | | \\  |')
    print('   |   |   | |   |       \\  /\\  /  | |  \\ |')
    print('   |   \\___/ \\___/        \\/  \\/   | |   \\|')
    
    board = default_board()
    
    board = randomize_key(board)
    
    
    
    valid_input = False
    while not valid_input:
        u_in = input('Would you like to play again? (Y/N): ')
        u_in = u_in.upper()
        
        
        if u_in == 'Y':
            valid_input = True
            
            
            return False, board
        elif u_in == 'N':
            valid_input = True
            print('Thanks for playing')
            return True, board
        else:
            print('Invalid Input')
    
def randomize_key(board):
    valid_location = False
    while not valid_location:
        
        x = random.randint(0,21)
        y = random.randint(0,21)
                
        if (board[y * -1])[x] == ' ':
            (board[y * -1])[x] = '~'
            valid_location = True
            return board

def concat_grids(grid_1, grid_2, row):
    temp_1 = grid_1[row]
    temp_2 = grid_2[row]
    
    new_list = ['*']
    
    for ele in temp_1:
        new_list.append(ele)
    for ele in temp_2:
        new_list.append(ele)
        
    new_list.append('*')
        
    return new_list
        

def default_board():
    
    grids = []
    
    p10 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    p9 = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*']
    
    p8 = ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', ' ', '*']
    
    p7 = ['*', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' ', ' ']
    
    p6 = ['*', '*', '*', '*', ' ', '*', ' ', ' ', ' ', ' ', '*']
    
    p5 = [' ', ' ', ' ', ' ', ' ', '*', ' ', '*', '*', ' ', ' ']
    
    p4 = ['*', ' ', '*', ' ', '*', '*', ' ', '*', ' ', ' ', '*']
    
    p3 = ['*', ' ', '*', ' ', ' ', ' ', ' ', '*', ' ', '*', '*']
    
    p2 = ['*', ' ', '*', ' ', '*', '*', '*', '*', ' ', '*', '*']
    
    p1 = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*']
    
    p0 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    grid = [p10, p9, p8, p7, p6, p5, p4, p3, p2, p1, p0]
    
    grids.append(grid)
    
    p10 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    p9 = ['*', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', '*', '*']
    
    p8 = ['*', '*', '*', ' ', '*', '*', ' ', '*', ' ', '*', '*']
    
    p7 = ['*', '*', '*', ' ', '*', '*', ' ', '*', ' ', '*', '*']
    
    p6 = ['*', '*', '*', ' ', ' ', ' ', ' ', '*', ' ', '*', '*']
    
    p5 = [' ', ' ', '*', '*', ' ', '*', '*', ' ', ' ', ' ', ' ']
    
    p4 = ['*', ' ', '*', '*', ' ', '*', '*', ' ', '*', '*', '*']
    
    p3 = ['*', ' ', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*']
    
    p2 = ['*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*']
    
    p1 = ['*', ' ', '*', ' ', '*', ' ', ' ', '*', '*', ' ', '*']
    
    p0 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    grid = [p10, p9, p8, p7, p6, p5, p4, p3, p2, p1, p0]
    
    grids.append(grid)
    
    p10 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    p9 = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*']
    
    p8 = ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', ' ', '*']
    
    p7 = ['*', ' ', ' ', ' ', ' ', '*', '*', '*', '*', ' ', '*']
    
    p6 = ['*', '*', '*', '*', ' ', '*', ' ', ' ', ' ', ' ', '*']
    
    p5 = [' ', ' ', ' ', ' ', ' ', '*', ' ', '*', '*', ' ', ' ']
    
    p4 = ['*', ' ', '*', '*', '*', '*', ' ', '*', ' ', ' ', '*']
    
    p3 = ['*', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*']
    
    p2 = ['*', ' ', '*', ' ', '*', '*', '*', '*', ' ', '*', '*']
    
    p1 = ['*', ' ', '*', ' ', ' ', ' ', ' ', '*', ' ', '*', '*']
    
    p0 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    grid = [p10, p9, p8, p7, p6, p5, p4, p3, p2, p1, p0]
    
    grids.append(grid)
    
    p10 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    p9 = ['*', ' ', ' ', ' ', ' ', ' ', '*', '*', ' ', '*', '*']
    
    p8 = ['*', ' ', '*', ' ', '*', ' ', '*', '*', ' ', '*', '*']
    
    p7 = ['*', '*', '*', ' ', '*', ' ', '*', '*', ' ', '*', '*']
    
    p6 = ['*', '*', '*', ' ', '*', ' ', ' ', '*', ' ', ' ', '*']
    
    p5 = [' ', ' ', ' ', ' ', '*', '*', ' ', ' ', ' ', ' ', ' ']
    
    p4 = ['*', ' ', '*', ' ', '*', '*', ' ', '*', '*', ' ', '*']
    
    p3 = ['*', '*', '*', '*', '*', '*', ' ', '*', '*', '*', '*']
    
    p2 = ['*', ' ', ' ', ' ', ' ', '*', ' ', '*', ' ', '*', '*']
    
    p1 = ['*', ' ', '*', '*', ' ', ' ', ' ', ' ', ' ', '*', '*']
    
    p0 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    grid = [p10, p9, p8, p7, p6, p5, p4, p3, p2, p1, p0]
    
    grids.append(grid)
    
    p10 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    p9 = ['*', ' ', ' ', '*', '*', ' ', '*', '*', ' ', '*', '*']
    
    p8 = ['*', ' ', '*', ' ', '*', ' ', '*', '*', ' ', ' ', '*']
    
    p7 = ['*', ' ', ' ', ' ', '*', ' ', '*', '*', '*', ' ', '*']
    
    p6 = ['*', '*', '*', ' ', '*', ' ', ' ', '*', '*', ' ', '*']
    
    p5 = [' ', ' ', ' ', ' ', '*', '*', ' ', ' ', ' ', ' ', ' ']
    
    p4 = ['*', ' ', '*', '*', '*', '*', ' ', '*', '*', ' ', '*']
    
    p3 = ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*']
    
    p2 = ['*', '*', '*', '*', '*', '*', ' ', '*', ' ', ' ', ' ']
    
    p1 = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*']
    
    p0 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    grid = [p10, p9, p8, p7, p6, p5, p4, p3, p2, p1, p0]
    
    grids.append(grid)
    
    p10 = ['*', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*', '*']
    
    p9 = ['*', ' ', '*', '*', '*', ' ', '*', '*', ' ', '*', '*']
    
    p8 = ['*', ' ', '*', ' ', '*', ' ', '*', ' ', ' ', ' ', '*']
    
    p7 = ['*', ' ', ' ', ' ', '*', ' ', '*', ' ', '*', ' ', '*']
    
    p6 = ['*', '*', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*']
    
    p5 = [' ', ' ', ' ', ' ', '*', '*', ' ', ' ', ' ', ' ', ' ']
    
    p4 = [' ', '*', '*', '*', '*', '*', ' ', '*', '*', ' ', '*']
    
    p3 = [' ', '*', ' ', '*', '*', ' ', ' ', '*', '*', '*', '*']
    
    p2 = [' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ']
    
    p1 = [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', '*']
    
    p0 = ['*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
    
    grid = [p10, p9, p8, p7, p6, p5, p4, p3, p2, p1, p0]
    
    grids.append(grid)
    
    used_grids = []
    
    valid_grid = False
    while not valid_grid:
        num = random.randint(0,(len(grids) - 1))
        if num not in used_grids:
            used_grids.append(num)
        if len(used_grids) >= len(grids):
            valid_grid = True
            
    grid_1 = grids[used_grids[0]]
    grid_2 = grids[used_grids[1]]
    grid_3 = grids[used_grids[2]]
    grid_4 = grids[used_grids[3]]
    
    p23 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    p0 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    
    p22 = concat_grids(grid_1, grid_2, 0)
    p21 = concat_grids(grid_1, grid_2, 1)
    p20 = concat_grids(grid_1, grid_2, 2)
    p19 = concat_grids(grid_1, grid_2, 3)
    p18 = concat_grids(grid_1, grid_2, 4)
    p17 = concat_grids(grid_1, grid_2, 5)
    p16 = concat_grids(grid_1, grid_2, 6)
    p15 = concat_grids(grid_1, grid_2, 7)
    p14 = concat_grids(grid_1, grid_2, 8)
    p13 = concat_grids(grid_1, grid_2, 9)
    p12 = concat_grids(grid_1, grid_2, 10)
    p11 = concat_grids(grid_3, grid_4, 0)
    p10 = concat_grids(grid_3, grid_4, 1)
    p9 = concat_grids(grid_3, grid_4, 2)
    p8 = concat_grids(grid_3, grid_4, 3)
    p7 = concat_grids(grid_3, grid_4, 4)
    p6 = concat_grids(grid_3, grid_4, 5)
    p5 = concat_grids(grid_3, grid_4, 6)
    p4 = concat_grids(grid_3, grid_4, 7)
    p3 = concat_grids(grid_3, grid_4, 8)
    p2 = concat_grids(grid_3, grid_4, 9)
    p1 = concat_grids(grid_3, grid_4, 10)
    
    
    board = [p23, p22, p21, p20, p19, p18, p17, p16, p15, p14, p13, p12, p11, p10, p9, p8, p7, p6, p5, p4, p3, p2, p1, p0]    
    (board[6])[-1] = '  $'
    (board[-3])[2] = '^'
    (board[6])[-2] = '|'

    return board

def forward(board, player, streak):
    
    x = player[0]
    y = player[1] + 1
    
    dest = (board[(y * -1) - 1])[x]
    
    if dest == '*' or dest == '|':
        (board[y * -1])[x] = ' '
        board, player, streak = death(board)

        print_board(board, streak)
 
    elif dest == '~':
        (board[6])[-2] = ' '
        player = [x, y]
        (board[(y * -1) - 1])[x] = '^'
        (board[y * -1])[x] = ' '
        
        print_board(board, streak)
    else:
        player = [x, y]
        (board[(y * -1) - 1])[x] = '^'
        (board[y * -1])[x] = ' '
    
        print_board(board, streak)
        
    return board, player, streak
    
def right(board, player, streak):
    
    terminate = False
    x = player[0] + 1
    y = player[1]
    
    dest = (board[(y * -1) - 1])[x]

    if dest == '*' or dest == '|':
        (board[(y * -1) - 1])[x - 1] = ' '
        board, player, streak = death(board)
        
        print_board(board, streak)
    elif dest == '  $':
        player = [x, y]
        (board[(y * -1) - 1])[x] = '  >'
        (board[(y * -1) - 1])[x - 1] = ' '
        streak += 1
        print_board(board, streak)
        

        terminate, board = win()
        if terminate == False:
            print_board(board, streak)

            player = [2, 2]
        
            
    elif dest == '~':
        (board[6])[-2] = ' '
        player = [x, y]
        (board[(y * -1) - 1])[x] = '>'
        (board[(y * -1) - 1])[x - 1] = ' '
        
        print_board(board, streak)
    else:
        player = [x, y]
        (board[(y * -1) - 1])[x] = '>'
        (board[(y * -1) - 1])[x - 1] = ' '
    
        print_board(board, streak)
        
        
        
    return board, player, streak, terminate
    
def down(board, player, streak):
    
    x = player[0]
    y = player[1] - 1
    
    dest = (board[(y * -1) - 1])[x]
    
    if dest == '*' or dest == '|':
        (board[(y * -1) - 2])[x] = ' '
        board, player, streak = death(board)

        print_board(board, streak)
    
    elif dest == '~':
        (board[6])[-2] = ' '
        player = [x, y]
        (board[(y * -1) - 2])[x] = ' '
        (board[(y * -1) - 1])[x] = 'v'
        
        print_board(board, streak)
    else:
        player = [x, y]
        (board[(y * -1) - 2])[x] = ' '
        (board[(y * -1) - 1])[x] = 'v'
    
        print_board(board, streak)
        
    return board, player, streak
    
def left(board, player, streak):
    
    x = player[0] - 1
    y = player[1]
    
    dest = (board[(y * -1) - 1])[x]
    
    if dest == '*' or dest == '|':
        (board[(y * -1) - 1])[x + 1] = ' '
        board, player, streak = death(board)

        print_board(board, streak)

    elif dest == '~':
        (board[6])[-2] = ' '
        player = [x, y]
        (board[(y * -1) - 1])[x] = '<'
        (board[(y * -1) - 1])[x + 1] = ' '
        
        print_board(board, streak)
    else:
        player = [x, y]
        (board[(y * -1) - 1])[x] = '<'
        (board[(y * -1) - 1])[x + 1] = ' '
    
        print_board(board, streak)
        
    return board, player, streak
    
def main():
    
    streak = 0
    
    board = default_board()
    
    board = randomize_key(board)
    
    print_board(board, streak)
    
    player = [2, 2]
    
    
    
    print()
    print('CONTROLS:')
    print('bot : have a rudimentary bot play for you')
    print('w : UP')
    print('d : RIGHT')
    print('s : DOWN')
    print('a : LEFT')
    print()
    
    terminate = False
    while not terminate:
        
        print('q : QUIT')
        user_inp = (input('> ')).lower()
        
        if user_inp == 'w':
            
            board, player, streak = forward(board, player, streak)
                
        elif user_inp == 'd':
            
            board, player, streak, terminate = right(board, player, streak)
                
        elif user_inp == 's':
            
            board, player, streak = down(board, player, streak)
                
        elif user_inp == 'a':
            
            board, player, streak = left(board, player, streak)
                
        elif user_inp == 'q':
            
            print('Thanks for playing')
            terminate = True
            
        elif user_inp == 'win':

            streak += 1
            print_board(board, streak)
            

            terminate, board = win()
            if terminate == False:
                print_board(board, streak)

                player = [2, 2]
                
        elif user_inp == 'bot':
            
            moves = []
            moves_2 = []
            moves_3 = []
            moves_4 = []
            count = 0
            
            stop = False
            while not stop:
                
                if count < 4:
                
                    x = player[0]
                    y = player[1]
                    
                    cur_time = time.time()
                    temp_time = time.time()
                    while (temp_time - cur_time) < 0.2:
                        temp_time = time.time()
                    
                    if ((board[(y * -1) - 1])[x + 1] == ' ' or (board[(y * -1) - 1])[x + 1] == '~' or (board[(y * -1) - 1])[x + 1] == '  $') and [x + 1, (y * -1) - 1] not in moves:
                        board, player, streak, terminate = right(board, player, streak)
                        temp = [x + 1, (y * -1) - 1]
                        moves.append(temp)
                    elif ((board[(y * -1) - 2])[x] == ' ' or (board[(y * -1) - 2])[x] == '~') and [x, (y * -1) - 2] not in moves:
                        board, player, streak = forward(board, player, streak)
                        temp = [x, (y * -1) - 2]
                        moves.append(temp)
                    elif ((board[(y * -1) - 1])[x - 1] == ' ' or (board[(y * -1) - 1])[x - 1] == '~') and [x - 1, (y * -1) - 1] not in moves:
                        board, player, streak = left(board, player, streak)
                        temp = [x - 1, (y * -1) - 1]
                        moves.append(temp)
                    elif ((board[(y * -1)])[x] == ' ' or (board[(y * -1)])[x] == '~') and [x, (y * -1)] not in moves:
                        board, player, streak = down(board, player, streak)
                        temp = [x, (y * -1)]
                        moves.append(temp)
                    else:
                        
                        if ((board[(y * -1) - 1])[x - 1] == ' ' or (board[(y * -1) - 1])[x - 1] == '~') and [x - 1, (y * -1) - 1] not in moves_2:
                            board, player, streak = left(board, player, streak)
                            temp = [x - 1, (y * -1) - 1]
                            moves_2.append(temp)
                        elif ((board[(y * -1) - 2])[x] == ' ' or (board[(y * -1) - 2])[x] == '~') and [x, (y * -1) - 2] not in moves_2:
                            board, player, streak = forward(board, player, streak)
                            temp = [x, (y * -1) - 2]
                            moves_2.append(temp)
                        elif ((board[(y * -1) - 1])[x + 1] == ' ' or (board[(y * -1) - 1])[x + 1] == '~' or (board[(y * -1) - 1])[x + 1] == '  $') and [x + 1, (y * -1) - 1] not in moves_2:
                            board, player, streak, terminate = right(board, player, streak)
                            temp = [x + 1, (y * -1) - 1]
                            moves_2.append(temp)
                        elif ((board[(y * -1)])[x] == ' ' or (board[(y * -1)])[x] == '~') and [x, (y * -1)] not in moves_2:
                            board, player, streak = down(board, player, streak)
                            temp = [x, (y * -1)]
                            moves_2.append(temp)
                        else:
                        
                            if ((board[(y * -1) - 1])[x - 1] == ' ' or (board[(y * -1) - 1])[x - 1] == '~') and [x - 1, (y * -1) - 1] not in moves_3:
                                board, player, streak = left(board, player, streak)
                                temp = [x - 1, (y * -1) - 1]
                                moves_3.append(temp)
                            elif ((board[(y * -1)])[x] == ' ' or (board[(y * -1)])[x] == '~') and [x, (y * -1)] not in moves_3:
                                board, player, streak = down(board, player, streak)
                                temp = [x, (y * -1)]
                                moves_3.append(temp)
                            elif ((board[(y * -1) - 1])[x + 1] == ' ' or (board[(y * -1) - 1])[x + 1] == '~' or (board[(y * -1) - 1])[x + 1] == '  $') and [x + 1, (y * -1) - 1] not in moves_3:
                                board, player, streak, terminate = right(board, player, streak)
                                temp = [x + 1, (y * -1) - 1]
                                moves_3.append(temp)
                            elif ((board[(y * -1) - 2])[x] == ' ' or (board[(y * -1) - 2])[x] == '~') and [x, (y * -1) - 2] not in moves_3:
                                board, player, streak = forward(board, player, streak)
                                temp = [x, (y * -1) - 2]
                                moves_3.append(temp)
                            else:
                            
                                if ((board[(y * -1) - 1])[x + 1] == ' ' or (board[(y * -1) - 1])[x + 1] == '~' or (board[(y * -1) - 1])[x + 1] == '  $') and [x + 1, (y * -1) - 1] not in moves_4:
                                    board, player, streak, terminate = right(board, player, streak)
                                    temp = [x + 1, (y * -1) - 1]
                                    moves_4.append(temp)
                                elif ((board[(y * -1)])[x] == ' ' or (board[(y * -1)])[x] == '~') and [x, (y * -1)] not in moves_4:
                                    board, player, streak = down(board, player, streak)
                                    temp = [x, (y * -1)]
                                    moves_4.append(temp)
                                elif ((board[(y * -1) - 1])[x - 1] == ' ' or (board[(y * -1) - 1])[x - 1] == '~') and [x - 1, (y * -1) - 1] not in moves_4:
                                    board, player, streak = left(board, player, streak)
                                    temp = [x - 1, (y * -1) - 1]
                                    moves_4.append(temp)
                                elif ((board[(y * -1) - 2])[x] == ' ' or (board[(y * -1) - 2])[x] == '~') and [x, (y * -1) - 2] not in moves_4:
                                    board, player, streak = forward(board, player, streak)
                                    temp = [x, (y * -1) - 2]
                                    moves_4.append(temp)
                                else:
                                    moves = []
                                    moves_2 = []
                                    moves_3 = []
                                    moves_4 = []
                                    count += 1
                        
                else:
                    print('oof, bot is stuck')
                    print("You'll need to take over for him")
                    stop = True
                        
        else:
            print_board(board, streak)
            print('Invalid input. Try again')

            
            
if __name__ == "__main__": 
    main()

