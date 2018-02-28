import random

def InitCoinSets():
    americanCoinsExtended = list({.01,.05,.1,.25,.50,1})   
    americanCoins = list({.01,.05,.1,.25,1})   
    americanCurrencyExtended = list(set(americanCoinsExtended).union({2,5,10,20,50,100}))
    americanCurrency = list(set(americanCoins).union({5,10,20}))
    return True

global americanCoinsExtended = americanCoinsExtended
global americanCoins = americanCoins
global americanCurrencyExtended = americanCurrencyExtended
global americanCurrency =a mericanCurrency

def InitSmallMonetaryVals():
    random.seed(True)
    listOfSmallMonetaryValues = []
    for i in range (0,10):
        listOfSmallMonetaryValues.append(random.uniform(0,3))
    return True

global listOfSmallMonetaryValues = listOfSmallMonetaryValues