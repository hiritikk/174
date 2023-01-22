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


def main():
    username = input('input usernamer ')
    valid_domains = ('gmail.com','ualberta.ca')
    check_username(username, valid_domains) #username, valid domains are arguments for the func
    
main()