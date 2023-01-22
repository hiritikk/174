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

def main():
    username = input('input usernamer ')
    valid_domains = ('gmail.com','ualberta.ca')
    valid_username = check_username(username, valid_domains) #username, valid domains are arguments for the func
    #check password
    if valid_username:
        password = input('Enter password > ')
        c_password = input('Enter password again > ')
        check_password_match (password , c_password)
    
main()