# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxLen = 0
        def findMax(root):
            nonlocal maxLen
            if not root :
                return 0
            
            leftMax = findMax(root.left)
            rightMax = findMax(root.right)

            maxLen = max(maxLen,(leftMax + rightMax))

            return 1 + max(leftMax, rightMax)
        findMax(root)
        return maxLen
        