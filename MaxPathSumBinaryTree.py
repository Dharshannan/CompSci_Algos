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

preorder = [-10,9,20,15,7]
inorder = [9,-10,15,20,7]
sol = Solution()
tree = sol.buildTree(preorder, inorder)

# Maximum path sum in a binary tree
maxsum = -float('inf')
def pathsum(node):
    global maxsum 
    if node is None:
        return(0)
    else:
        lpath = pathsum(node.left)
        rpath = pathsum(node.right)
        maxsum = max(node.val, node.val + max(lpath,rpath), node.val + lpath + rpath,maxsum)
        return(max(node.val, node.val + max(lpath,rpath)))

pathsum(tree)
print(maxsum)

# Inorder traversal using recursion
def trav(root):
    if root is None:
        return ([])
    
    lpath = trav(root.left)
    rpath = trav(root.right)
    inorder = lpath + [root.val] + rpath
    return(inorder)

print(trav(tree))

# Inorder traversal iteratively
stack = []
results = []
while (tree is not None) or (stack !=[]):
    while tree is not None:
        stack.append(tree)
        tree = tree.left
    s = stack.pop()
    tree = s.right
    results.append(s.val)
    
print(results)


