import requests, pprint

def get_currency_name(code):
    url= 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    
    

def main():
    url = 'https://api.exchangerate.host/latest'

    cur_from = 'CAD'
    cur_to = ['INR','KWD','EUR','UZS','PKR','GEL']
    amount =  float(input("Enter the amounnt in cad  "))
    while True:
        currency_code = input('Enter the currency code or just press enter to stop')
        if currency_code == '':
            break
        cur_to.append(currency_code)
    
    payload = {'base':cur_from, 'symbols': ','.join(cur_to), 'amount': amount}
    response = requests.get(url,payload)
    data = response.json()
    
    for code,amount in rates.items():
        name = get_currency_name(code)
        print(f'{round(amount,2)} {name}')

if __name__ == '__main__':
    main()

