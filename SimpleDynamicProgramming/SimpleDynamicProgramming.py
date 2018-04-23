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
    root = TreeNode(0)
    for i in range(0, len(coins), 1):
        if amount-coins[i]>=0:
            root.addChild(TreeNode(coins[i]))
    #call helper method to build tree of all possible payments from root
    for i in range(0, len(root.children), 1):
        mkChHelper(root.children[i], amount-root.children[i].getValue, coins)

    return getShortestDepth(root)[0]

def getShortestDepth(root):
    if(root.children==[]):
        return [[root.value], 1]
    smallest = getShortestDepth(root.children[0])
    for i in range(1, len(root.children),1):
        current = getShortestDepth(root.children[i])
        if(current[1]<smallest[1]):
            smallest=current
    smallest[0].append(root.value)
    print(smallest[0])
    return [smallest[0], smallest[1]+1]

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