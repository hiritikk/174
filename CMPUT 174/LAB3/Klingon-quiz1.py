'''

In this program we translate a word in klingon to english 

'''

fobj = 'klingon-english.txt'    # This holds our file in a variable
mode = 'r'

with open (fobj) as file:       # Here it opens the file using the "with open()" method
    line1=file.readline()
    line2=file.readline()
    line3=file.readline()

find = line3.find('|')         # This helps to find the translated word from our text file, which is used as a refernce point to slice the word from the text file later

extract = line3[0:find]        # extract stores the location of the translated word in a variable

input_language=input('How do you translate computer to klingon?')

'''
Here we check if the entered word is the correct translation of klingon word
'''
if input_language == extract :
    print('correct!')
else:
    print("Sorry you are wrong! ")
    print("The correct answer is De'wI'")