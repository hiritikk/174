pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901
alist=[29 ,51 , 589 ,  2901]
name = input(" Enter the name of the character ")
age = int(input("enter teh age "))


if age < 0 :
    print(" invalid age")
elif age < 29:
    print(f' {name} is {age} and is younger than Pippin, Frodo, Gollum and Arwen')
elif age > 51 and age < 289:
    print(f' {name} is {age} and is older than Frodo and Pippin but is younger than Arwen and Gollum')
elif age > 589 and age < 2901:
    print(f' {name} is {age} and is older than Gollum, Pipin and Frodo but is younger than Arwen')
elif age > 2901:
    print(f' {name} is {age} and is older than Frodo, Pippin, Arwen and Gollum')


