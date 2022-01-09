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

preorder = [25,15,10,4,12,22,18,24,50,35,31,44,70,66,90]
inorder = [4,10,12,15,18,22,24,25,31,35,44,50,66,70,90]
sol = Solution()
tree = sol.buildTree(preorder, inorder)

# Recursive preorder
def preorder(node,res):
    if node is None:
        return
    res.append(node.val)
    preorder(node.left,res)
    preorder(node.right,res)
    return(res)
print(preorder(tree,[]))

# Iterative preorder
def itr(node,res):
    stack = []
    stack.append(node)
    while len(stack) > 0:
        node = stack.pop()
        res.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return(res)
print(itr(tree,[]))

# Postorder recursion
def postorder(node,res):
    if node is None:
        return
    postorder(node.left, res)
    postorder(node.right, res)
    res.append(node.val)
    return(res)

print(postorder(tree,[]))
    
# Post order iterative
def peek(stack):
    if len(stack) > 0:
        return(stack[-1])
    return

def itr2(node,res):
    if node is None:
        return([])
    stack = []
    while True:
        while node is not None:
            if node.right is not None:
                stack.append(node.right)
            stack.append(node)
            node = node.left
        node = stack.pop()
        if node.right is not None and peek(stack) == node.right:
            stack.pop()
            stack.append(node)
            node = node.right
            
        else:
            res.append(node.val)
            node = None
            
        if len(stack) <= 0:
            break
        
    return(res)
print(itr2(tree,[]))

# Recursive inorder 

def inorder(node,res):
    if node is None:
        return
    inorder(node.left,res)
    res.append(node.val)
    inorder(node.right,res)
    return(res)

print(inorder(tree,[]))

# Inorder iterative

def ino(node,res):
    stack = []
    while node is not None or stack != []:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node = node.right
    return(res)

print(ino(tree,[]))

