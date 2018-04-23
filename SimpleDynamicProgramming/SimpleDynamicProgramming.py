import sys
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def getValue(self):
        return self.value

    def getChildren(self):
        return self.children    

def mkCh(amount, coins):
    #this algorithm will brute-force the problem to find all coin combinations, and then choose the smallest amount
    #create first level of tree
    root = []
    for i in range(0, len(coins), 1):
        if amount-coins[i]>=0:
            root.append(TreeNode(coins[i]))
    #call helper method to build tree of all possible payments from root
    for i in range(0, len(root), 1):
        mkChHelper(root[i], amount-root[i].getValue, coins)

    return change

def mkChHelper(node, amount, coins):
    for i in range(0, len(coins), 1):
        if amount-coins[i]>=0:
            node.getChildren.append(TreeNode(coins[i]))
    return None
if __name__ == "__main__":
    #coinset used
    coins = [1,5,10,25]
    #amount needed to pay, in cents
    amount = 41
    #make change
    change = mkCh(amount, coins)
    #output
    print("Amount Change Needed For: " + str(amount))
    print("Optimal Payment: " + str(change))
    sum = 0
    for i in range(0, len(change), 1):
        sum = sum+change[i]
    print("Was it payable? " + str(sum==amount))