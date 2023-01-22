frodo_age = 51
gollum_age = 589
def func():
    ch= input(" Enter the character's name- ")
    age = int(input(" Enter the age of the character- "))

    if age == 51 or age == 589:
        print(f'{ch.capitalize()} is {age} years old, and is the same age as Frodo and Gollum.')
    elif age < 51 and  age > 589:
        print(f'{ch.capitalize()} is {age} years old, and is younger than Frodo but is older than Gollum.')
    elif age > 51 and age < 589:
        print(f'{ch.capitalize()} is {age} years old, and is older than Frodo but is younger than Gollum.')
    elif age > 51 and age > 589:
        print(f'{ch.capitalize()} is {age} years old, and is older than both Frodo and Gallum.')
    elif age < 51 and age < 589:
        print(f'{ch.capitalize()} is {age} years old, and is younger than both Frodo and Gollum.')        
    
    opt = input(" Do you want to run it again? (y/n): ")
    if opt == 'y':
        func()
    else:
        print("Thank You!")
        

        
func()

