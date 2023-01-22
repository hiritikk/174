

klingon_consonants=[ "b", "ch", "D", "gh", "H", "j", "l", "m", "n", "p", "q", "Q", "r", "S", "t", "v", "w", "y","'"]

import random
fobj = 'klingon-english.txt'
mode = 'r'
file = open(fobj, mode) 
count = 3

consonant = input("Which consonant do you want to practice with ? ")
# This while loop will make sure the right consonant is typed and if wrong, it will ask again to type
while True:                                                                 
    if consonant in klingon_consonants:                                      
        break
    else:
        consonant = input('Please enter a valid Klingon Consonant -->')

# Using readlines we read all the lines in the file         
data = file.readlines()                                                      

# For loop runs the entered consonant throughout the file to find the corresponding words
for i in range(len(data)) :                                                 
    if data[i][0] == consonant[0] :
        find = data[i].split('|')
        # we use strip() to remove the whitespace character from the extracted word.
        print("Translate",find[1].strip(),"to klingon")                      
        trans = input("-->")
        # Compares the inputted translated word(trans) with the given klingon word in the list
        if trans == find[0] :                                                
            print("correct")
            # break Stops the for loop here if the consonant is correct
            break
        else:
            print(" Sorry you are wrong,The correct answer is ", find[0] )
            klang = find[0]
            
            hintStart = klang[0:1]
            klang = list(klang)
            aterisk = klang[1:-1] = '*' * len(klang[1:-1])
            hintEnd = klang[-1]

            print("Hint:", hintStart + aterisk + hintEnd)
            secondTry = input("->")

            # second try
            if secondTry == find[0]:
                print("Correct!")
            else:   #count helps to count the attempt remaining
                count -= 1   
                print("Incorrect!, How do you translate",find[0],"to klingon "+str(count)+" attempt left.\n")
                print("Hint:", hintStart + aterisk + hintEnd)

                # third try
                rand = random.randrange(len(klang[1:-1]))   # finds random number
                rand = int(rand)
                index = rand + 1
                randLetter = find[0][index]   # finds the random character
                lastHint = hintStart+aterisk+hintEnd
                lastHint = list(lastHint)
                lastHint[index] = randLetter   # replaces aterisk with the newly found random character
                finalHint = ''
                for i in lastHint:   # changes lastHint from list to string
                    finalHint += ''+i
                print("Hint:", finalHint)
                finalAnswer = input("->")                
                finalanswer = input("->")
                if finalanswer == find[0]:
                    print("Correct!")
                else:
                    count -= 1
                    print("Incorrect!, How do you translate",find[0],"to klingon "+str(count)+" attempt left.\n")    
                    
file.close()
