#amortization calculator

def invest(amount, rate, year, addl):
    i = 1
    if addl.lower() == 'manual':
        while i <= year:
            addl = float(input(f"Please enter additional amount you will invest in year {i}: "))
            amount = amount + amount * rate + addl  
            print(f"Total at year {i}: ${amount:,.2f}")
            i = i + 1  
    else:
        while i <= year:
            amount = amount + amount * rate + float(addl)
            print(f"year {i}: ${amount:,.2f}")
            i = i + 1
    
amount = float(input('Please enter your initial amount: '))
rate = (float(input('Please enter your expected rate of return: ')))/100
year = float(input('Please enter years you plan to hold account: '))
addl = input('Please enter yearly addition or type manual: ')
invest(amount, rate, year, addl)