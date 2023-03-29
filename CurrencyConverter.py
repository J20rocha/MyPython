
currencies = {'Euro': 1.0, 'Dollar': 1.07184, 'Pound': 1.14292, 'Yen': 0.00711}

def converter(amount, currencyfrom, currencyto):
    if currencyfrom not in currencies or currencyfrom == currencyto or currencyto not in currencies:
        return "Invalid operation"
    
    result = (amount*currencies[currencyto])/currencies[currencyfrom]
    return result

if __name__ == "__main__":
    while True:
        currencyfrom= input("Currency from: ")
        currencyto = input("Currency to: ")
        amount= float(input("Amount: "))
        result=converter(amount, currencyfrom, currencyto)
        print("Result= " + str(result))
        
        