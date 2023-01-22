"""
this code checek the typing speed
"""

import time
import random 

def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    data1 = []    # a list to append enter all the stripped words here
    fobj = open( filename, 'r') 
    data = fobj.readlines() # .readlines() reads all the line and returns a list of the words
    for i in data: data1.append(i.rstrip('\n'))
    fobj.close()
    return data1
    
    
def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    data = read_spells('spells.txt')
    for lst in data:
        data_random = random.choice(data) # random.choice() choses random words from the file 
    return data_random
    

def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    print("#" * 60)
    print("Harry Potter Typing Trainer")
    print("#" * 60)
    
    
    

def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    filename = "instructions.txt"
    fobj = open(filename , 'r')
    data = fobj.readline()
    while data:
        print(data.strip())
        data = fobj.readline()
    fobj.close()
    
    

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    if user_input == spell:
        print("Correct")
        print(f'You get 10 points!', end = "")
        
    else:
        print("Incorrect!")
        print("The spell was" + str(spell))
        print("You lose! ", end ="")
        

def play_again() -> bool:
    """
    Asks the user if they want to play again
    Returns True if the user enters Y or y, False otherwise
    """             
    global while_value
    while_value = True
    
    reply = input('continue y/n ').lower()
    response = reply == 'y'
    if response:
        return True
    else:
        return False



def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """
    TTT = len(spell) * 0.3
    return TTT

def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    """
   
def main() -> None:
    """
    Main program.
    """
    while_value = True
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    score = 0 
    
    
    while while_value:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        value = display_feedback(spell,user_input)
        if value == 1:
            score += 10 
            print(f'Your score is {score}')
            
        else:
            score -= 5
            print(f'Your score is {score}')
            
        while_value = play_again()
    print(f'Your final score is {score}')
        
main()

