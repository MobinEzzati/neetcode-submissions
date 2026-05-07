# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depthCalculator(root, leftDepth, rightDepth): 
            if not root :
                return 0 
            
            leftMax = depthCalculator(root.left,leftDepth,rightDepth)
            righMax = depthCalculator(root.right,leftDepth,rightDepth)

            return 1 + max(leftMax,righMax)
        return depthCalculator (root,0,0)
        
        