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

# Node to node path
# Using recursive dfs 
def dfs(node,n,visited,path):
    if node is None:
        return
    visited.append(node.val)

    if node.val == n:
        path.append([i for i in visited])
        
    dfs(node.left,n,visited,path)
    dfs(node.right,n,visited,path)
    visited.pop()
    for itm in path:
        return itm
    
path1 = dfs(tree,9,[],[])
path2 = dfs(tree,20,[],[])

# Find intersection between each path
intersection = []
for item in path1:
    for items in path2:
        if item == items:
            intersection.append(item)
# Trim off list till point of intersection and add the lists together to get the node to node path         
point_int = intersection[-1]
index1 = path1.index(point_int)
index2 = path2.index(point_int)

path1 = path1[index1:]
path2 = path2[index2+1:]

node_path = path1[::-1] + path2
print(node_path)


