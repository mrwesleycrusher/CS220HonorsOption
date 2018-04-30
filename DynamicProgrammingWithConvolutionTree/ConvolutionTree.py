def mkCh(amount, coins):
    #start with an empty list
    combos = []
    #start with all possibilites of one coin
    for i in range(0, len(coins), 1):
        combos.append([coins[i]])
    while True:
        #check to see if amount can be paid yet
        currentCombo = checkComplete(amount, combos)
        #if the amount can't be paid by a permutation, create new permutations
        if (currentCombo == None):
            combos = recombine(combos, coins)
        #in the case the amount cannot be paid with the current coin system, return none
        elif (combos == []):
            return None
        else:
            return currentCombo

def checkComplete(amount, combos):
    #check if a permutation has paid the amount, and remove all the ones that went bust
    for i in range(0, len(combos), 1):
        sum=0
        for j in range( 0, len(combos[i]), 1):
            sum = sum + combos[i][j]
        if amount == sum:
            return combos[i]
        if sum > amount:
            combos.remove(combos[i])
            i = i - 1
    return None

def recombine(combos, coins):
    #add every coin value to the end of the list that contains the previous n coin values
    newCombos = []
    for i in range(0, len(combos), 1):
        for j in range(0, len(coins), 1):
            newCombos.append(combos[i] + [coins[j]])
           
    return newCombos
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
    sum = 0
    for i in range(0, len(change), 1):
        sum = sum+change[i]
    print("Was it payable? " + str(sum==amount))