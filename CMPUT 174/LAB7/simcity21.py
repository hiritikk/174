

def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    # TODO: Implement this function
    filename = 'data_1.txt'
    fobj = open(filename,'r')
    cobj = fobj.read()
    cobj=cobj.split('\n') #removes end line spaces
    
    matrix = []
    x = 0 
    rows = int(cobj[0]) # first value of the list as rows
    cols = int(cobj[1])# second value of the lsit as columns
    
    
    for i in range(rows):
        row = []
        for j in range(x,cols):
            a = int(cobj[j+2])
            row.append(a)
        cols+= rows # incrementing by the number of rows/cols as both values are same 
        x+= rows # incrementing by the number of rows
        matrix.append(row)
    return matrix



def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values
    """
    # TODO: Implement this function
    
    for row in grid:
        a_row = ''
        for col in row:
            a_row += str(f"{col:8}") #formatimng by 4 spaces
        print(f"{a_row:8}")  
    return a_row




def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    neighbour_list=[]
    a_rows = len(grid)
    b_cols = len(grid[0])
    
    for index in range(row-1, row+2):  
        for j in range(col-1, colx+2):  
            #if it completes the for condition it moves on 
            if index == row and j == col:
                #and is used so it satisfies both conditions 
                continue    # shifts to the next part of the code
            if index < 0 or index >= a_rows or j < 0 or j >= b_cols:
                continue  # shifts to the next part of the code
            neighbour_list.append(grid[index][j])
    return neighbour_list
#used the format of the code from practice question of our class,

def main() -> None:
    """
    Main program.
    """
    
    grid = create_grid("data_1.txt")
    print("\nSim City Land Values:")
    display_grid(grid)
    

 
main()