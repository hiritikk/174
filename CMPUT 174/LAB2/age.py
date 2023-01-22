ch= input(" Enter the character's name ")
age = int(input(" Enter the age of the character "))
frodo_age = 51

if age == 51: 
    print(f'{ch.capitalize()} is {age} years old, and is the same age as Frodo.')
else:
    if age < 51:
        print(f'{ch.capitalize()} is {age} years old, and is younger than Frodo.')
    elif age > 51:
        print(f'{ch.capitalize()} is {age} years old, and is older than Frodo.')
        

