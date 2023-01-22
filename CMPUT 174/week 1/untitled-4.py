'''#Ratburn1# input-function
#fucntions may take arguments - expressions that is within the round brackets
temperature = float(input(" Enter the temp --> "))

if temperature < -5:
    print("Students shall wear there jackets")
print(" Enter the classroom ")


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
#Ratburn2
name = input(' ENter the name of the student ')

if name[0] >='A' and name[0] <= 'M':
    side = 'left'
else: 
    side='right'
print(name,'Will be the seated in the',side,'of the classroom')

'''
'''
#Ratburn3

classavg=float(input(" Enter the classs average. "))

if classavg <= 40 :
    treat = ' lollipop '
elif classavg <= 90 :
    treat = ' cookie '
elif classavg > 90:
    treat = ' ice cream'
    
print(" According to class average ya'll deserve",treat)

#4
marks=float(input("Enter marks- >"))
grade= ' '

if marks < 0 or marks > 100:
    print("Mark is not valid")
else: 
    if marks >=0 :
        grade = 'F'
    elif marks >= 50 :
        grade = 'D'
    elif marks >= 60 :
        grade = 'C'
    elif marks >= 70:
        grade = 'B'
    elif marks <= 80:
        grade = 'A'    
    print('grade is', grade)
'''
quiz_mark =int(input("enter marks of the quiz"))
changed = False
if quiz_mark >= 50:
    p_level = input("participation level")
    if p_level =='A':
        percent = 0.2
    elif p_level == 'U':
        percent = 0.15
    elif p_level == 'S':
        percent = 0.10
    elif p_level == 'R':
        percent = 0.05
    else:
        percent=0
    
    new_quiz = quiz_mark + quiz_mark * percent
    if new_quiz != quiz_mark:
        changed = True
        
if changed:
    print("new quiz mark is",new_quiz)
else:
    print('quiz mark remain unchanged')
    
