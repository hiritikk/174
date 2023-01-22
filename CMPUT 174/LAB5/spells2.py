"""
This code prints the instructions for te game and is a follow up of the spells1.py which prints the random word from the file
"""

import random 

def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    data1 = []
    fobj = open( filename, 'r')   #Opens the file with the words
    data = fobj.readlines()
    for i in data: data1.append(i.rstrip('\n')) #removes whitespace characters 
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
        print(data.strip())    # Removes white space characters 
        data = fobj.readline()
    fobj.close()
    
    

def get_user_input(spell: str) -> str:
    """
    Gets the spell as input from the user and returns it.
    """
    user_input = input(f'Enter the following spell: {spell}\n') # \n shifts the input to a new line
    return user_input


def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    if user_input == spell:
        print("Correct")     
    else:
        print("Incorrect!, The correct word is" + str(spell))
        
        

def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)


main()