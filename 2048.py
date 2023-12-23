## In Progress ##
# 2048 Game

import random

board_template = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]


def create_random_coords():
    '''
    Creates random coordinates to randomize the starting board
    '''
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    return x, y


def create_starting_board():
    '''
    Creates starting board with random two boxes getting assigned 2
    Returns: new list for the starting board
    '''
    coords = create_random_coords()
    starting_board = board_template.copy()
    starting_board[coords[0]][coords[1]] = 2
    coords2 = create_random_coords()
    if coords2 == coords:
        templist = [i for i in range(4)]
        templist.remove(coords[1])
        coords2 = (coords2[0], random.choice(templist))
    starting_board[coords2[0]][coords2[1]] = 2
    return starting_board


def print_board(board):
    '''
    Prints list of numbers in the format of the 2048 4x4 board
    '''
    print('\n')
    print('-' * 41)
    for row in board:
        print('|         |         |         |         |')
        for index, element in enumerate(row):
            if index == 0:
                print(f'| {element:^7} | ', end='')
            elif index == 3:
                print(f'{element:^7} | ')
            else:
                print(f'{element:^7} | ', end='')
        print('|         |         |         |         |')
        print('-' * 41)
    print('\n')




def find_empty_spaces(board):
    '''
    Finds coords of empty spaces
    Returns: list of all coords as tuples
    '''
    empty_spaces_list = []
    for index, row in enumerate(board):
        for index1, element in enumerate(row):
            if element == ' ':
                empty_spaces_list.append((index, index1))
    return empty_spaces_list


def add_two(board):
    '''
    Adds a two to a random empty space
    Returns: list substituting a random empty space with a 2
    '''
    randomindex = random.randint(0, len(find_empty_spaces(board)))
    board[find_empty_spaces(board)[randomindex-1][0]
          ][find_empty_spaces(board)[randomindex-1][1]] = 2
    return board


def move_to_empty_space(board, input):
    '''
    Repeatedly checks for open squares then moves to that square based off input
    '''
    if input == 'w':
        for i in range(6):
            for index, row in enumerate(board):
                for index1, element in enumerate(row):
                    if index != 0 and board[index-1][index1] == ' ':
                        board[index-1][index1] = element
                        board[index][index1] = ' '
    elif input == 'a':
        for i in range(6):
            for index, row in enumerate(board):
                for index1, element in enumerate(row):
                    if index1 != 0 and board[index][index1 - 1] == ' ':
                        board[index][index1-1] = element
                        board[index][index1] = ' '
    elif input == 's':
        for i in range(6):
            for index, row in enumerate(board):
                for index1, element in enumerate(row):
                    if index != 3 and board[index+1][index1] == ' ':
                        board[index+1][index1] = element
                        board[index][index1] = ' '
    elif input == 'd':
        for i in range(6):
            for index, row in enumerate(board):
                for index1, element in enumerate(row):
                    if index1 != 3 and board[index][index1 + 1] == ' ':
                        board[index][index1+1] = element
                        board[index][index1] = ' '
    return board


def move_merge(board, input):
    '''
    Merges numbers that are equal to eachother into one square that is double the value. 
    '''
    if input == 'w':
        for index, row in enumerate(board):
            for index1, element in enumerate(row):
                if index != 0 and board[index-1][index1] == board[index][index1] and type(board[index][index1]) == int:
                    board[index-1][index1] = element * 2
                    board[index][index1] = ' '
    elif input == 'a':
        for index, row in enumerate(board):
            for index1, element in enumerate(row):
                if index1 != 0 and board[index][index1 - 1] == board[index][index1] and type(board[index][index1]) == int:
                    board[index][index1-1] = element * 2
                    board[index][index1] = ' '
    elif input == 's':
        for index, row in enumerate(board):
            for index1, element in enumerate(row):
                if index != 3 and board[index+1][index1] == board[index][index1] and type(board[index][index1]) == int:
                    board[index+1][index1] = element * 2
                    board[index][index1] = ' '
    elif input == 'd':
        for index, row in enumerate(board):
            for index1, element in enumerate(row):
                if index1 != 3 and board[index][index1 + 1] == board[index][index1] and type(board[index][index1]) == int:
                    board[index][index1+1] = element * 2
                    board[index][index1] = ' '
    return board


def main():
    game_continuing = True
    pracboard = create_starting_board()
    print_board(pracboard)

    while game_continuing:
        user_input = input("Enter a move (W/A/S/D): ").lower() 
        if user_input in ['w', 'a', 's', 'd']:
            move_to_empty_space(pracboard, user_input)
            move_merge(pracboard, user_input)
            move_to_empty_space(pracboard, user_input)
            add_two(pracboard)
            print_board(pracboard)
        else:
            print('\n',"Please play using WASD keys", '\n')
        
        for row in pracboard:
            if 2048 in row:
                print('Congratulations, you\'ve reached 2048!', '\n', '\n')
                game_continuing = False

        element_counter = 0
        for row in pracboard:
            for element in row:
                if element != ' ':
                    element_counter += 1
        if element_counter == 16:
            print('You Lost!', '\n', '\n')
            game_continuing = False


main()
