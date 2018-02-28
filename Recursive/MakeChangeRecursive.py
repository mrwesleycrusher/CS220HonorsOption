import CoinSystems
CoinSystems.InitCoinSets
CoinSystems.InitSmallMonetaryVals

def MakeChange(value, coinSystem):
    change = []
    while (value > 0):
        for i in range(len(coinSystem),0,1):
            if(value - coinSystem[i]) > 0:
                value = value - coinSystem[i]
                change.append(coinSystem[i])
                i = len(coinSystem)
                continue
    return change

MakeChange( listOfSmallMonetaryValues[0], americanCoinsExtended)