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
    return board

def display_board(board):
    ''' displays the board |0|0|0|'''
    display_str = '|'
    for index in range(len(board)):
        display_str = f'{display_str}{board[index]}|'
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))
        
def roll_die(sides):
    '''rolls a die'''
    input('press enter to roll')
    number = random.randint(1,sides)
    return number
        


def main():
    board_size = int(input(" Enter the size of the boards > "))
    board = create_board(board_size)
    display_board(board)
    sides = int(input(" How many side do you want your die to have > "))
    value = roll_die(sides)
    print(f'you rolled{value}')
    
    
    
    
main()