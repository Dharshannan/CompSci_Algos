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

# Recursive code to yield all root-to-leaf paths
list1 = []
def dfs(stack,node):
    if node is None:
        return
    stack.append(node.val)
    if (node.left is None) and (node.right is None):
        list1.append([i for i in stack])  # for some odd reason list1.append(stack) doesnt work
        
    dfs(stack,node.left)
    dfs(stack,node.right)
    stack.pop()
        
dfs([],tree)
print(list1)







        