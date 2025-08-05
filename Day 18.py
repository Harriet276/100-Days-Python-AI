##Day 18: Trees – Binary Trees & Inorder Traversal ##

#Building a binary tree

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None



root = TreeNode(5)
root.left = TreeNode(3)
root.right= TreeNode(7)
root.left.right = TreeNode(4)
root.left.left = TreeNode(1)
root.right.right = TreeNode(9)

treeList= []
def inorder_Traversal(node):

    if node is not None:
        inorder_Traversal(node.left)
        print(node.val , end = '')
        inorder_Traversal(node.right)



inorder_Traversal(root)
print("    \n")

# LeetCode Practice
# LeetCode – 94. Binary Tree Inorder Traversal
# ➡️ You’ll be asked to return the inorder traversal as a list.


def inorder_TraversalList(node):
    if node is None:
        return []
    else:
        return  inorder_TraversalList(node.left) + [node.val] + inorder_TraversalList(node.right)


treeList =inorder_TraversalList(root)
print(treeList)