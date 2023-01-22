pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901
older_list = []
young_list =[]
same_list=[]
alist=[29 ,51 , 589 ,  2901]
name = input(" Enter the name of the character ")
age = int(input("enter teh age "))

for i in alist(4):
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


"""
for i in range(3):
    if alist[i] > age:
        print(f'character is{age} and is younger than 1 2 3 4')
    elif:
        print(f'character is {age} but is older than 

        
      
        
        
        
        

for i in range(4):
    if alist[i]==age:
        same_list.append(alist[i])
        print(alist[i])
for k in range(4):
    if alist[i]>age:
        older_list.append(alist[k])
    else:
        young_list.append(alist[k])
        alist.pop(same_list)
    '''else:
        if alist[i]>age:
            older_list.append(alist[i])
            alist.pop(same_list)
        else:
            young_list.append(alist[i])
            alist.pop(same_list)'''
print(older_list)
print(young_list)
"""