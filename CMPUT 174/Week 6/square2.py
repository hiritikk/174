'''
V4 - dispaly_results
V3 - is_game_over
V2 - update
V1 - create_boards, display board, roll_die

'''

Game_piece = "#"



import random
def create_board(size:int)->list:
    ''' creates a board with given size '''
    board = [0] * size
    return create_board

def display_board(board:list, game_piece_pos:int)->none:
                                                              ''' displays the board |0|0|0|'''
    display_str = '|'
    
    for index in range(len(board)):
        if index == game_piece_pos:
        display_str = f'{display_board}{board[index]}|'
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))
        
def roll_die(sides):
    '''rolls a die'''
    input('press enter to roll')
    number = random.randint(1,sides)
    return number
        
#v2
def update(board:list, current_position:int, value_of_roll:int)->int:
                                          ''' updates the board by incrementing the number of visits to the square'''
    new_position = (current_position + value_of_roll) % len(board)
    board[new_position] = board[new_position] + 1 
    return new_position



def main():
    current_position = -1  # the positioon is off the board 
    board_size = int(input(" Enter the size of the boards > "))
    board = create_board(board_size)
    display_board(board, current_position)
    sides = int(input(" How many side do you want your die to have > "))
    value = roll_die(sides)
    print(f'you rolled{value}')
    current_position = update_board(board,current_position,value_of_roll):
    
    
    
main()