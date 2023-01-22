"""
this code prints a matrix of the list in the file
"""

def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    # TODO: Implement this function
    filename = 'data_0.txt'
    fobj = open(filename,'r')
    cobj = fobj.read()
    cobj=cobj.split('\n') #removes end line spaces
    
    matrix = []
    x = 0 
    rows = int(cobj[0]) # first value of the list as rows
    cols = int(cobj[1])# second value of the lsit as columns
    

def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values
    """
    # TODO: Implement this function
    
    for row in grid:
        a_row = ''
        for col in row:
            a_row += str(f"{col:4}") #formatimng by 4 spaces
        print(f"{a_row:10}")  
        


def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("\nSim City Land Values:")
    display_grid(grid)

 
main()