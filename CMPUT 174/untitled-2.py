'''
The average amount of. Hours worked by all emo is 21.5
Dob,david wonder more than 21.5 hours per week 
'''


# .strip() remover whitecharacters from end of line 
# .split() splits a sentence to elements of a lst, if entered a "," it will strip after every comma
filename= ‘employee.text'
more = 'r'
#open file
with open(filename , mode) as file :  #file is an identifier bound ti a textIOwrapper type object
    list_of_lines = file.readlines() # reads all lines and retorn a list of lines

for line in list_of_lines:
    line = line.strip()
    record = line.split()
    hours = 0
    for index in range(1, len(record)):
        hours += int(record[index])
    print(f'{record[0]}, {hours} ${hours * pay_rate}')
    
