"""
This is a follow up code for spell2.py which shows the scores of the game and reduces the score by 5 and increments by 10 if the answer is correct
"""
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
    data = fobj.readline() # reads file line by line 
    while data:
        print(data.strip())
        data = fobj.readline()
    fobj.close()
    
    

def get_user_input(spell: str) -> str:
    """
    Gets the spell as input from the user and returns it.
    """
    user_input = input(f'Enter the following spell: {spell}\n')
    return user_input

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    value = 0                   # using flag variable we are able to confirm the correct or incorrect answer 
    if user_input == spell:
        print("Correct")
        print(f'You get 10 points!', end = "")
        value = 1               # If its correct 
    else:
        print("Incorrect!")
        print("The spell was" + str(spell))
        print("You lose! ", end ="")
    return value                # returns 0 is incorrect 
        

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
    
    
def main() -> None:
    """
    Main program.
    """
    while_value = True
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    score = 0                   # flag variable to confirm correct or incorrect answer
    
    while while_value:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        value = display_feedback(spell,user_input)
        if value == 1:
            score += 10 # increments the score by 10 
            print(f'Your score is {score}')
            
        else:
            score -= 5  # if incorrect reduces the score by 5
            print(f'Your score is {score}')
            
        while_value = play_again() # won't run if the flag variable is false
    print(f'Your final score is {score}')
        
main()




        
'''
if display_feedback(spell) == 'Correct' :
        score += 10
        print(f'You get 10 points! Your score is {score}')
        play_again()
    else:
        print(display_feedback(spell))
        score -= 10
        print(f'You lose! Your score is {score}')
        play_again()
        
        
        
        
    
    # TODO: Implement scoring system
    # After the game is over, display the final score
    
main()
'''
