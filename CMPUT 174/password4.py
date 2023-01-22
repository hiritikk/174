def check_username( username, valid_domains ):
    is_valid = False
    if username.count('@') == 1:
        record = username.split('@')
        domain = record[1]
        if domain in valid_domains:
            is_valid = True
            print('username is valid')
    if not is_valid:
        print(' Username is not vaild!!! ' )
    
    return is_valid #throw which is a true or false


def check_password_match ( pass1 , pass2 ): # name of the argument does not have to be the same as the parameter
    match = False
    if pass1 == pass2:
        match = True
    if not match:
        print(" Passwords do not match " )    
    return match 

def check_length(pass2 ,length):
    has_len = False
    if len(pass2) >= length:
        has_len = True
    if not has_len:
        print(" Password is not 8 characters long " )
    return has_len   #throw true or false

    

def check_digit(password):
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        print(" Password is missing a digit " )
    return has_digit
    
    
def check_capital(password):
    has_capital = False
    for char in password:
        if char.isupper():
            has_capital = True
    if not has_capital:
        print(" Password is missing a capital")
    return check_capital
            
            
def check_special(password):
    has_special = False
    for char in password:
        if char.isalnum():
            has_special = True
            break
    if not has_special:
        print(" Password is missing a special character ")
    return has_special # throws true or false


def main():
    username = input('input usernamer ')
    valid_domains = ('gmail.com','ualberta.ca')
    length = 8
    valid_username = check_username(username, valid_domains) #CATCH #username, valid domains are arguments for the func
    registered = False
    while not registered:
        #check password
        if valid_username:
            password = input('Enter password > ')
            c_password = input('Enter password again > ')
            confirmed = check_password_match (password , c_password)
            if confirmed:
                has_length = check_length(password, length)
                has_digit = check_digit (password)
                has_capital = check_capital(password)
                has_special = check_special(password)
                if has_capital and has_digit and has_length and has_special:
                    print(" Registration is successful :) " )
                    registered = True
                
        
    
main()