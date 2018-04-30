import sys
#treenode object
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
        mkChHelper(root.children[i], amount-root.children[i].getValue(), coins)

    return getShortestDepth(root)[0][:-1]

#optimizes the solution by finding the lowest depth in the tree
def getShortestDepth(root):
    #if leaf node return value
    if(root.children==[]):
        return [[root.value], 1]
    #otherwise grab leftmost child
    smallest = getShortestDepth(root.children[0])
    #find the shortest subtree, with each child being a root
    for i in range(1, len(root.children),1):
        current = getShortestDepth(root.children[i])
        if(current[1]<smallest[1]):
            smallest=current
    smallest[0].append(root.value)
    #return the shortest subtree you find
    return [smallest[0], smallest[1]+1]

#build tree of all possible ways of paying the amount
def mkChHelper(node, amount, coins):
    for i in range(0, len(coins), 1):
        if amount-coins[i]>=0:
            newChild = TreeNode(coins[i])
            node.getChildren().append(newChild)
            mkChHelper(newChild, amount-coins[i], coins)
    return None

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