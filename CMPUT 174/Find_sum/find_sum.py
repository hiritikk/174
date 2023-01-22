# write a function that adds all numbers in a list
# Fuction should return if list is empty
# Function return none if the parameter is not a list object 
# Fucntion shoudl also return None is any of the item in the ilist isnt a int


def add_number(alist):
    if isinstance(alist, list):         # isinstance(identifier, type that needs to be checked)    # imp Quiz 3
        return None                 
    if alist == []:
        return None
    sum_of_numbers = 0
    
    for number in alist:
        if not isinstance(number,int):
            return None
        sum_of_numbers += number
    return sum_of_numbers

def main():
    blist = [2,4,6]
    add_number(blist)
    print(add_number(blist))

if __name__ == '__main__':  # Quiz 3
    main()