###### Tic Tac Toe game ######
import random
print('\n' * 2)
print('**************************************************')
print('Welcome to the best Tic Tac Toe game ever players')
print('**************************************************')
print('\n' * 2)

def display_board(board):
    print(' ' +   board[7]   + ' | ' +   board[8]   + ' | ' +   board[9]  )
    print('-----------')
    print(' ' +   board[4]   + ' | ' +   board[5]   + ' | ' +   board[6]  )
    print('-----------')
    print(' ' +   board[1]   + ' | ' +   board[2]   + ' | ' +   board[3]  )

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Please user choose your marker between [X,O]: ").upper()
    if turn == 'Player 1' and marker == 'X':
        return ('X', 'O')
    elif turn == 'Player 1' and marker == 'O':
        return ('O', 'X')
    elif turn == 'Player 2' and marker == 'X':
        return ('O', 'X')
    elif turn == 'Player 2' and marker == 'O':
        return ('X', 'O')


def marking_board(board, marker,position):
    board[position] = marker

def player_choice(board):
    position = None
    while not position in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_space(board,position):
        position = int(input('Please select ' + turn + ' in which position you desire to put your marker [1-9]: '))
    return position

def win(board, marker):
    return(board[1] == marker and board[2] == marker and board[3] == marker or board[4] == marker and board[5] == marker and board[6] == marker or
    board[7] == marker and board[8] == marker and board[9] == marker or board[1] == marker and board[4] == marker and board[7] == marker or
    board[2] == marker and board[5] == marker and board[8] == marker or board[3] == marker and board[6] == marker and board[9] == marker or
    board[1] == marker and board[5] == marker and board[9] == marker or board[7] ==  marker and board[5] == marker and board[3] == marker)

def check_space(board, position):
     return board[position] == ' '

def board_full(board):
    for i in range(1,10):
        if check_space(board, i):
            return False
    return True

def replay():
    play = input('Do you want to play again? yes/no: ')
    return play


gaming = True
while gaming:
    print('Board with its positions')
    print('\n' * 1)
    print(' ' + '  7  ' + ' | ' + '  8   ' + ' | ' + ' 9  ')
    print('------------------------')
    print(' ' + '  4   ' + '| ' + '  5   ' + ' | ' + ' 6  ')
    print('------------------------')
    print(' ' + '  1   ' + '| ' + '  2   ' + ' | ' + ' 3  ')
    print('\n')
    turn = choose_first()
    print(turn + ' goes first')
    player1_marker, player2_marker = player_input()
    game_on = True
    the_board = ['#'] + [' ']*9
    while game_on:
        #User1 turn
        if turn == 'Player 1':
            position = player_choice(the_board)
            marking_board(the_board, player1_marker, position)
            print('\n')
            display_board(the_board)
            print('\n')

            if win(the_board, player1_marker):
                print('****************************************************')
                print('Congratulations! '+ turn + ' You have won the game')
                print('****************************************************')
                print('\n')
                game_on = False

            else:
                if board_full(the_board):
                    print('****************************************************')
                    print('Sorry! the game is draw!')
                    print('****************************************************')
                    print('\n')
                    game_on = False

                else:
                    turn = 'Player 2'

        else:

            position = player_choice(the_board)
            marking_board(the_board, player2_marker, position)
            print('\n')
            display_board(the_board)
            print('\n')

            if win(the_board, player2_marker):
                print('****************************************************')
                print('Congratulations! '+ turn + ' You have won the game')
                print('****************************************************')
                print('\n')
                game_on = False

            else:
                if board_full(the_board):
                    print('****************************************************')
                    print('Sorry! the game is draw!')
                    print('****************************************************')
                    print('\n')
                    game_on = False

                else:
                    turn = 'Player 1'
    
    if replay() == 'yes':
        print('\n')
        print('Restarting the game....')
        print('\n')
        print('**********WELCOME AGAIN**********')
        gaming = True
        print('\n' * 3)

    else:
        print('\n')
        print('Goodbye then')
        gaming = False

print('\n')
print('*****END*****')
