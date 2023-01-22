filename = 'employees.txt"
mode = 'r'

file = open(filename, mode)
content = file.read()
print(content)
file.close()

#method 1 - read the entire content of the file 
one_line = file.readline()
print(one_line)

#method 3 - view the file as a sequence of lines
for line in file:
    print(line)
    
    
#methods 4 - readlines methods

list_of_lines = file.readlines()        #returns as a list





































