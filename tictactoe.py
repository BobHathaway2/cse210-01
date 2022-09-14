'''
    Author: Bob Hathaway
    Course: CSE 210
    Class: Fall 2022, Section 18
    Assignment: W01 Prove: Developer, Tic-Tac_Toe
'''
import random
board_array = []
board_dimension = 3

def initialization():
    global board_array
    global board_dimension
    board_array = [[0 for i in range(board_dimension)] for j in range(board_dimension)]
    square_number = 1
    for i in range(board_dimension):
        for j in range(board_dimension):
            board_array[i][j] = square_number
            square_number += 1
    if random.random() >= 0.5:
        current_player = 'X'
    else:
        current_player = 'O'
    return current_player
        
def determine_row_column_from_selected_value(selected_value):
    global board_dimension
    row_value = (selected_value - 1) // board_dimension
    column_value = (selected_value - 1) % board_dimension
    return row_value, column_value

def is_selection_available(selected_square):
    global board_array
    global board_dimension
    row_value, column_value = determine_row_column_from_selected_value(selected_square)
    if board_array[row_value][column_value] == selected_square: # if value hasn't changed to an x or o
        return True
    else:
        return False

def get_players_selection(player):
    valid_selection = False
    while not valid_selection:
        try:
            players_selection = int(input (f'{player}\'s turn to choose a square (1-9): '))
            if players_selection >=1 and players_selection <= 9:
                valid_selection = is_selection_available(players_selection)
                if not valid_selection:
                    print('That\'s not an available square. Try again...')
            else:
                print('Oops!  That was not a valid square.  Try again...')
        except:
            print('That\'s not a number.  Try again...')
    return players_selection

def display_board():
    print ()
    global board_array
    global board_dimension
    for i in range(board_dimension):
        for j in range(board_dimension):

            if j < board_dimension - 1:
                print (f'{board_array[i][j]}', end ='|')
            elif i < board_dimension - 1:
                print (f'{board_array[i][j]}')
                for k in range(0,board_dimension,2):
                    print('-+', end = '')
                print('-')
            else:
                print(board_array[i][j])
    print ()

def store_players_selection(current_player, players_selection):
    global board_array
    row_value, column_value = determine_row_column_from_selected_value(players_selection)
    board_array [row_value] [column_value] = current_player

def determine_result_of_play(current_player, players_selection):
    global board_array

    result = ''
    row_value, column_value = determine_row_column_from_selected_value(players_selection)
    # check horizontal
    
    print(f'{board_array[row_value][0]} {board_array[row_value][1]} {board_array[row_value][2]}') 
    if (board_array[row_value][0] == board_array[row_value][1]) and (board_array[row_value][2] == board_array[row_value][1]): 
        result = 'Winner'
    # check vertical
    elif (board_array[0][column_value] == board_array[1][column_value]) and (board_array[0][column_value] == board_array[2][column_value]):
        result = 'Winner'
    elif (row_value == column_value and column_value == 1) or (board_array[1][1] == current_player): # check the diagnals
        if (board_array[0][0] == current_player) and (board_array[2][2] == current_player) or \
             (board_array[0][2] == current_player) and (board_array[2][0] == current_player):
             result = 'Winner'
    return result

def main():
    global board_array

    game_over = False
    move_count = 0
    current_player = initialization()
    display_board()
    while not game_over:
        players_selection = get_players_selection(current_player)
        store_players_selection(current_player, players_selection)
        move_count += 1
        result_of_play = determine_result_of_play(current_player, players_selection)
        display_board()
        if result_of_play == 'Winner':
            print(f'Congratulations Player {current_player}, you\'ve won the game!')
            game_over = True
        elif move_count == board_dimension ** 2:
            print('The game has ended with no winner - it\'s a draw! Great job to both of you!')
            game_over = True
        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
    print()


if __name__ == '__main__':
    main()
