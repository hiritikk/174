import requests, pprint

def main():
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json() # json() method is same as loads()
        print(type(data))
        rates = data["rates"]
        print(f'1 Euro = {rates["KWD"]}KWD')
        
    
    
if __name__ == '__main__':
    main()

