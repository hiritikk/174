filename = "employees_c.txt"
mode = 'r'
pay_rate = 20
 
employees = []
weekly_hours = []
above_average = []
 
 

#def func():  # inside the parantheses is parameters

with open(filename, mode) as file:
    list_of_lines = file.readlines()
for line in list_of_lines:
    #remove the leading and trailing blanks from the line 
    line = line.strip()
    # split the line to create a list of words
    record = line.split()
    
    if record: # process record only if its not an empty list
        name = record[0] # name is the first item in the record list 
        employees.append(name)
        # add all the hours starting from position 1 until the end of the list 
        hours = 0 
        for index in range(1, len(record)):
            hours = hours + int(record[index])
        weekly_hours.append(hours)
        print(f'{name} {hours} ${hours * pay_rate}')
        
print(employees)
print(weekly_hours)
average = sum(weekly_hours)/len(weekly_hours)
print(average)

for index in range(len(weekly_hours)):
    if weekly_hours[index] > average:
        above_average.append(employees[index])
print (','.join(above_average)) # , is a seperator that sep the words with

    
    # arguments & parameters 
    # function is evaluted in the order its written in, but no, function is evaluated only and only if fucntion is called 
    # every funtion in pythin returns an object, sometimes the object doesnt return anything which is none 
    # even if theres not return, it will return a none 
    
"""
doubts

how return works in functions and none 
read 1-25
"""
        
        
