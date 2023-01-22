
def decrypt_caesar(text: str, shift: int) -> str:
    """
    This fucntion will shift the ascii values 
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
    
def main() -> None:
    
    text = input("Enter a text to decipher: ")
    print("Let's try all the methods we have:")   
    result = decrypt_caesar(text,3)
    result1 = decrypt_atbash(text)
    print(result)
    print(result1)

main()

`#HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV.