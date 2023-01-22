'''
In this program we locate the klingon word with their consonants and translate it to english based on the consonants 

'''


klingon_consonants=[ "b", "ch", "D", "gh", "H", "j", "l", "m", "n", "p", "q", "Q", "r", "S", "t", "v", "w", "y","'"]

fobj = 'klingon-english.txt'
mode = 'r'
file = open(fobj, mode)  

consonant = input("Which consonant do you want to practice with ? ")

while True:                                                                 
    if consonant in klingon_consonants:                                     # break Stops the for loop here if the consonant is correct 
        break
    else:
        consonant = input('Please enter a valid Klingon Consonant -->')
        
data = file.readlines()                                                      # Using readlines we read all the lines in the file 

for i in range(len(data)) :                                                  # For loop runs the entered consonant throughout the file to find the corresponding words
    if data[i][0] == consonant[0] :
        find = data[i].split('|')
        print("Translate",find[1].strip(),"to klingon")                      # we use strip() to remove the whitespace character from the extracted word.
        trans = input("-->")
        if trans == find[0] :                                                # Compares the inputted translated word(trans) with the given klingon word in the list
            print("correct")
            break
        else:
            print(" Sorry you are wrong","The correct answer is ", find[0] )
file.close()
