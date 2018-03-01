import random

americanCoinsExtended = None
americanCoins = None
americanCurrencyExtended = None 
americanCurrency = None
listOfSmallMonetaryValues = None
def InitCoinSets():
    global americanCoinsExtended
    global americanCoins
    global americanCurrencyExtended 
    global americanCurrency
    americanCoinsExtended = list({.01,.05,.1,.25,.50,1})   
    americanCoins = list({.01,.05,.1,.25,1})   
    americanCurrencyExtended = list(set(americanCoinsExtended).union({2,5,10,20,50,100}))
    americanCurrency = list(set(americanCoins).union({5,10,20}))
    return True



def InitSmallMonetaryVals():
    global listOfSmallMonetaryValues
    random.seed(True)
    listOfSmallMonetaryValues = []
    for i in range (0,10):
        listOfSmallMonetaryValues.append(random.uniform(0,3))
    return True


