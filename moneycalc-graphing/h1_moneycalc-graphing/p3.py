'''Turn dollars into coins'''

# ctrl-c ctrl-z don't affect the console for me
while True:
    try:
        cash_str = input('Enter Amount: ')
        cash = float(cash_str) * 100
        cash_int = int(cash)
        q = 25 # quarter
        d = 10 # dime
        p = 1  # penny
        quarters = cash_int // q
        cash_int -= (quarters * q)
        dimes = cash_int // d
        cash_int -= (dimes * d)
        pennies = cash_int // p
        cash_int -= (pennies * p)
        print('Quarters: ', quarters)
        print('Dimes: ', dimes)
        print('Pennies: ', pennies)
        print('Total: ', (quarters + dimes + pennies))
        print('Total money in coins:', cash_str)
    except ValueError:
        print("Invalid Input: Terminating...")
        break
