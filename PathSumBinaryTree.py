#Binary tree path sum (targetsum)
# Path is going down

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

# Path sum using 2 helpers

count = 0 #count paths that sum up to taget sum
targetSum = 27

def helper1(node,curr):
    global count
    if node is None:
        return
    curr += node.val
    if curr == targetSum:
        count += 1
    
    helper1(node.left,curr)
    helper1(node.right,curr)
    
def helper2(node):
    if node is None:
        return
    helper1(node,0)
    helper2(node.left)
    helper2(node.right)
    
helper2(tree)
print(count)    
