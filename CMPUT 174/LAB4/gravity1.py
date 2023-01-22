"""
In this code we decrypt a encrypted code inputted by the user
"""
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
            x = (lower.index(character)-shift) % len(lower)
            result += lower[x]
        else:
            result += character
    return result
    
def main() -> None:
    
    text = input("Enter a text to decipher: ")
    shift = int(input(" By how much do you want to shift >"))
    print(decrypt_caesar(text,shift))
main()















#VWDQ LV QRW ZKDW KH VHHPV.