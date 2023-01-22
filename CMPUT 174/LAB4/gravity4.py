"""
in this function we combine all the previous codes
"""
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
    return result    




def decrypt_a1z26(text: str) -> str :
    """
    Decipher a text (A1Z26 cipher).
    """
    result = ""      
    data = text.upper().split() # convert the word to uppercase (as per instructions) and split by spaces first
    for character in data: 
        data_2 = character.split("-") # then, split each unit by hyphens for the numbers
        for character_2 in data_2:
            if character_2.isnumeric(): # if the unit is a digit, then cast it into an integer and add 64 to get the uppercase equivalent character
                character_2 = chr(int(character_2) + 64)    
            result += character_2  
        result += " " # add a space for the space that has been removed during splitting
    return result       



    
def main() -> None:
    """
    this is the main function that runs all the functions one after the other 
    """
    
    text = input("Enter a text to decipher: ")          # takes inout from user
    shift=int(input("Enter how much do you want to shift the characters > "))   # values to shift by 
    print("Let's try all the methods we have:")   
    
    print("Caesar cipher: " + decrypt_caesar(text,shift))
    print("Atbash cipher: " + decrypt_atbash(text))
    print("Combined: 1) Caesar; 2) Atbash cipher: " + decrypt_atbash(decrypt_caesar(text,shift)))
    print("Combined: 1) Atbash; 2) Caesar cipher: " + decrypt_caesar(decrypt_atbash(text),shift))
    print("A1Z26 cipher: " + decrypt_a1z26(text))
    print("Combined: 1) A1Z26; 2) Caesar cipher: " + decrypt_caesar(decrypt_a1z26(text),shift))
    print("Combined: 1) A1Z26; 2) Caesar cipher: " + decrypt_atbash(decrypt_a1z26(text)))
    print("Combined: 1) A1Z26; 2) Atbash; 3) Caesar cipher: " + decrypt_caesar((decrypt_atbash(decrypt_a1z26(text))),shift))
    print("Combined: 1) A1Z26; 2) Atbash; 3) Caesar cipher: " + decrypt_atbash(decrypt_caesar(decrypt_a1z26(text),shift)))

main()

# 22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1.

