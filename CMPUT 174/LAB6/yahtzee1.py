"""
In this code we see the making of the yahtzee game, with dices of Aces,Twos,Threes,Fours,Fives,Sixes
"""
def make_roll() -> tuple:
    """
    Returns a tuple of five random values between 1 and 6.
    """
    import random
    randomlist = random.sample(range(1, 6), 5) # Here we generate a random tuple of 6 elements
    a_tuple = tuple(randomlist) #converting to a tuple
    return a_tuple



def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    """
    Sum = 0
    for num in roll:
        if num == number:
            Sum = number + Sum # Summition of all the values
    return Sum 
 

def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    """
    Aces = sum_of_given_number(roll,1)         
    Twos = sum_of_given_number(roll,2)
    Threes = sum_of_given_number(roll,3)
    Fours = sum_of_given_number(roll,4)
    Fives = sum_of_given_number(roll,5)
    Sixes = sum_of_given_number(roll,6)
    blist = [Aces,Twos,Threes,Fours,Fives,Sixes]
    return blist



def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    print("Aces: ", upper_section_scores[0])    # Here we use subscription for getting the values from the list of the dices
    print("Twos: ", upper_section_scores[1])
    print("Threes: ",upper_section_scores[2])
    print("Fours: ", upper_section_scores[3])
    print("Fives: ", upper_section_scores[4])
    print("Sixes: ", upper_section_scores[5])    

def main():
    """
    Main function.
    """
    print("Rolling the dice....",make_roll())
    print("Upper section: ")
    value_roll= make_roll()
    value_upper = fill_upper_section(value_roll)  #sending values of value_upper to the function fill_upper_section
    display_upper_section(value_upper)


if __name__ == "__main__":
    main()