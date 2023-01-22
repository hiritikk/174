MAP_FILE = 'cave_map.txt'


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
        x = 0
        rows = len(cobj_rows) 
        cols = len(cobj_cols) 
        
        for i in range(rows):
            alist = []
            for j in range(x,cols):
                a = file.read(1)
                alist.append(a.strip())
            grid.append(alist)
            while '' in alist:  #to remove emoty string from the list 
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


def main():
    """
    Main entry point for the game.
    """
    # TODO: implement the main() function


    grid = load_map(MAP_FILE)
    print(grid)
    start = find_start(grid)
    print("starting position", start)
    get_command()
    
if __name__ == '__main__':
    main()
