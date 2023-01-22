'''
This code reads the file and then prints randomly slelected words from the file
'''


import random 

def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    fobj = open( filename, 'r')     # Opens the file with the words
    data = fobj.readlines()
    fobj.close()
    return data  #throw
    
    
    
def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    data = read_spells('spells.txt') # Stores the code in a variable 
    data_random = random.choice(data) # random.choice() choses random words from the file 
    return data_random.lower()
    
    
def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')  #catch
    print('Harry Potter Keyboard Trainer')
    spell = get_random_spell(spells)
    print(spell)

main()
