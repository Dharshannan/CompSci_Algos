#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return(None)
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return(root)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol = Solution()
tree = sol.buildTree(preorder, inorder)

# Try to append this values into a list using breadth first search
# This gives back the preorder traversal (bfs) but is actually the layered/level traversal

results = []
def bfs(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while len(stack)>0:
        results.append(stack[0].val)
        node = stack.pop(0)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
            
    return(results)

print(bfs(tree))
        
# Lets try the above using resursion     

#lets 1st find the height of the tree
def height(node):
    if node is None:
        return(0)
    else:
        lheight = height(node.left)+1
        rheight = height(node.right)+1
        
    if lheight > rheight:
        return(lheight)
    else:
        return(rheight)
    
# Next lets get a function for appending nodes for each level
results1 = []
def leveltra(root,level):
    if root is None:
        return
    if level == 1:
        results1.append(root.val)
    elif level > 1:
        leveltra(root.left,level-1)
        leveltra(root.right,level-1)
        
def heighttra(root):
    h = height(root)
    for i in range(1,h+1):
        leveltra(root, i)
    return(results1)

    
print(heighttra(tree))