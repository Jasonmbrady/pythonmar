#mplement generateCoinChange(cents) that accepts a parameter for the number of cents, and computes how to represent that amount with the smallest number of coins. Print out each coin (Quarters, dimes, nickels, pennies) and the quantity of each.

def coin_change(cents):
    quarters = 0        # Initialize number of each coin to 0
    dimes = 0
    nickels = 0
    pennies = 0
    while cents >= 25:  # check if at least one quarter can be generated
        quarters += 1 
        cents -= 25     # Take one quarter out and check the while condition again
    while cents >= 10:  # check if at least one dime can be generated
        dimes += 1
        cents -= 10     # Take one dime out and check the while condition again
    while cents >= 5:   # check if at least one nickel can be generated
        nickels += 1
        cents -= 5      # Take one nickel out and check the while condition again
    while cents > 0:    # check if at least one penny can be generated
        pennies += 1
        cents -=        # Take one penny out and check the while condition again
    print(f"Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, Pennies: {pennies}") # print out results

coin_change(99)
coin_change(65)
coin_change(74)