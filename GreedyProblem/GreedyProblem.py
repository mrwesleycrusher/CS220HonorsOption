import sys

def mkCh(amount, coins):
    #this will be the optimal list of coins for payment
    change = []
    #we will start at the largest coin value
    index = len(coins) - 1
    #we will stop when we reach 0 cents
    while(amount>0):
        #if we can use the coin we have currently selected, subtract it from the amount left, our pocket, and continue
        if amount >= coins[index]:
            amount = amount - coins[index]
            change.append(coins[index])
        #otherwise, try a smaller coin
        else:
            index = index -1
    return change

if __name__ == "__main__":
    #coinset used
    coins = [1,3,4]
    #amount needed to pay, in cents
    amount = 6
    #make change
    change = mkCh(amount, coins)
    #output
    print("Amount Change Needed For: " + str(amount))
    print("Optimal Payment: " + str(change))
    print("True Optimal Payment: [3,3]")
    sum = 0
    for i in range(0, len(change), 1):
        sum = sum+change[i]
    print("Was it payable? " + str(sum==amount))