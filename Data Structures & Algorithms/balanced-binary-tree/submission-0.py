# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        
        def height(node):
            if not node:
                return -1  # height of empty subtree
            return 1 + max(height(node.left), height(node.right))
        
        if root is None:
            return True  # ✅ empty tree is balanced
        
        left = height(root.left)
        right = height(root.right)
        
        # ✅ root.left and root.right are TreeNodes
        if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False
