MAP_FILE = 'cave_map.txt'

from copy import deepcopy 

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    # TODO: implement this function

    with open(map_file,'r') as file:
        
        cobj_rows = file.readlines()
        file.seek(0)
        cobj_cols = file.readline()
        file.seek(0)
        grid = []
        x=0
        rows = len(cobj_rows) 
        cols = len(cobj_cols) 

        for i in range(rows):
            alist = []
            for j in range(x,cols):
                a = file.read(1)
                alist.append(a.strip())
            grid.append(alist)
            
            while '' in alist:  # to remove emoty string from the list 
                alist.remove('')        
                        
        return grid 



def find_start(grid: list[list[str]]) -> list[int, int]:
    for alist in grid:
        for things in alist:
            if things == 'S':
                x = grid.index(alist) # Row
                y = alist.index('S') # column
                
    start = [x,y]
    return start
                
def get_command() -> str:
    """
    Gets a command from the user.
    """
    # TODO: implement this function
    while True:
        command = input("Enter escape to quit: ")
        if command.lower() == "escape":
            break   
        else:
            print(" I do not understand ")

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    # TODO: implement this function
    blist = deepcopy(grid)
    for alist in blist:
        for things in alist:
            if things == 'S':
                a = alist.index('S')
                alist[a] = '@'
    for i in blist:  # selects lists from the list
        space = ''
        for y in i:  # chooses elements from the list within the list
            space += str(y) + ' '  # adds them into a string format
        print(space)
            


def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    # TODO: implement this function
    rows = len(grid)
    cols = len(grid[0])
    return [rows,cols]  
    

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    # TODO: implement the rest of the function
    rows_=position[0]
    cols_=position[1]
    if rows_>=0 and rows_<grid_rows:
        if cols_>=0 and cols_<grid_cols:
            return True
    return False
    
    
    
def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
        
    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
        directions.append('west')

    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects: 
        directions.append('east')

    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:  
        directions.append('south')

    return directions    

def main():
    """
    Main entry point for the game.
    """
    # TODO: update the main() function
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)
    size = get_grid_size(grid)
    while True:
        direction = ' '.join(map(str,look_around(grid,player_position)))
        print("you can go", str(direction))        
        user_input = input("")
        if user_input.lower() == "show map":
            display_map(grid, player_position)
            print("you can go", str(direction))  
            pass
        elif user_input == "escape":
            get_command()
        else:
            print("Invalid input")
        
            
if __name__ == '__main__':
    main()
