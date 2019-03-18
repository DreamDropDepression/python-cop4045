# Homework 1
# Problem 3 solution
#
#  Do not distribute.
#
denominations = [25,10,1]   # for quarters, dimes, pennies
# if we wanted nickels then this list should be  [25,10,5,1]

den_names = ["quarters", "dimes", "pennies"]

while True:
    amount = float(input('Enter amount:'))

    if amount < 0:
        print("Invalid input.")
    else:
        # convert to pennies:
        amount_cents = int(amount * 100)


        # we compute the count for each denomination in a loop:
        coin_count = []
        coins_total_amount = 0
        coins_total_count = 0
        cents_left = amount_cents

        msg = "$" + str(amount) + " makes "   # to be printed

        for d in range(0, len(denominations)):
            den = denominations[d]
            n = cents_left // den
            coin_count.append(n)
            coins_total_count += n
            cents_left -= n * den
            coins_total_amount += n * den

            msg += str(n) + " " + den_names[d] + ", "

        print(msg + " (" + str(coins_total_count) + " coins) total amount in coins: $"
              + str(coins_total_amount / 100) + ".")


    
