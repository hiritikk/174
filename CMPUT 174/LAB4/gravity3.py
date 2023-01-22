
def decrypt_caesar(text: str, shift: int) -> str:
    """
    This fucntion will shift the ascii values and decrypt it
    """
    global result
    low= "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # coverts string to list 
    upper=list(up)
    lower=list(low)
    result= ''
    for character in text:
        if character in upper:
            # x is letter of the character which is in alphabet in formula (x-n) mod 26
            x = (upper.index(character)-shift) % len(upper)
            result += upper[x]
        elif character in lower:
            # x is letter of the character which is in alphabet in formula (x-n) mod 26
            x = (lower_alph.index(character)-shift) % len(lower)
            result += lower[x]
        else:
            result += character
    return result

def decrypt_atbash(text: str) -> str:
    """
    This function will decrypt the given input to readable format 
    """
    
    global result1
    
    low= "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # coverts string to list 
    upper=list(up)
    lower=list(low)
    # empty string to store the result 
    result1= ''
    for character in text:
        if character in upper:
            # x is letter of the character which is in alphabet in formula (x-n) mod 26
            x = -(upper.index(character)+1) % len(upper)
            result1 += upper[x]
        elif character in lower :
            # x is letter of the character which is in alphabet in formula (x-n) mod 26
            x = -(lower.index(character)+1) % len(lower)
            result1 += lower[x]
        else:
            result1 += character
    return result1    

def decrypt_a1z26(text: str) -> str :
    result = ""      
    data = text.upper().split() # convert the word to uppercase (as per instructions) and split by spaces first
    for character in data: 
        data_2 = character.split("-") # then, split each unit by hyphens for the numbers
        for character_2 in data_2:
            if character_2.isdigit(): # if the unit is a digit, then cast it into an integer and add 64 to get the uppercase equivalent character
                character_2 = chr(int(character_2) + 64)    
            result += character_2  
            print(result)
            
        result += " " # add a space for the space that has been removed during splitting
    return(result)        



    
def main() -> None:
    """
    this is the main function that runs all the functions one after the other 
    """
    
    text = input("Enter a text to decipher: ") # takes inout from user
    print("Let's try all the methods we have:")   
    result = decrypt_caesar(text,3)
    result1 = decrypt_atbash(text)
    print("Caesar cipher: " + result)
    print("Atbash cipher: " + result1)    
    print("A1Z26 cipher: " + decrypt_a1z26(text))


main()

# 22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1.

'''
[[1,2,3],2,3,4,5]
'''
