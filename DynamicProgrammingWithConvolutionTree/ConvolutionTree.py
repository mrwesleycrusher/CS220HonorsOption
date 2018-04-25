def mkCh(amount, coins):
    combos = []
    for i in range(0, len(coins), 1):
        combos.append([coins[i]])
    while True:
        currentCombo = checkComplete(amount, combos)
        #print(combos)
        if (currentCombo == None):
            combos = recombine(combos, coins)
        elif (combos == []):
            return None
        else:
            return currentCombo

def checkComplete(amount, combos):
    for i in range(0, len(combos), 1):
        sum=0
        for j in range( 0, len(combos[i]), 1):
            sum = sum + combos[i][j]
            #print(sum)
        if amount == sum:
            return combos[i]
        if sum > amount:
            combos.remove(combos[i])
            i = i - 1
    return None

def recombine(combos, coins):
    newCombos = []
    for i in range(0, len(combos), 1):
        for j in range(0, len(coins), 1):
            newCombos.append(combos[i] + [coins[j]])
            #print(combos[i])
            #print(coins[j])
            #print(newCombos)
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