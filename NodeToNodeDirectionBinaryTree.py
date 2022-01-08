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

# LCA (Lowest Common Ancestor) and node to node directions

def lca(node,n1,n2):
    if node is None:
        return
    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if node.val == n1 or node.val == n2:
        return node

    l = lca(node.left,n1,n2)
    r = lca(node.right,n1,n2)
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if l and r:
        return node
    # Otherwise check if left subtree or right subtree is LCA
    return l if l is not None else r
    
# Get root to node path
def path(node,val,results,s):
    if node is None:
        return
    if node.val == val:
        s.append([i for i in results]) 
    results.append('L')
    path(node.left,val,results,s)
    results.pop()
    results.append('R')
    path(node.right,val,results,s)
    results.pop()
    for item in s:
        return(item)
    
# Get node to node path
def pathshit(node, start, end):
    lc = lca(node,start,end)
    path1 = path(lc,start,[],[])
    path2 = path(lc,end,[],[])
    for i in range(len(path1)):
        path1[i] = 'U'
        
    fullpath = path1 + path2
    return(fullpath)

full_path = ''.join(pathshit(tree,-10,20))
print(full_path)
    

    
    
    


    