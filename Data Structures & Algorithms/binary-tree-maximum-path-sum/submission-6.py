# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # some form of dfs with a nonlocal max that get's updated every time a new 
        # node is explored with some max(curMax, node.val) 
        # and the dfs working such that every path is explored in a dfs manner. 
        # Also could think of some form of width of bt edge cases and 
        # approaches to ensure we consider every possible path

        res = float("-inf")

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right)) 
            
            res = max(res, left + right + node.val)

            return node.val + max(left, right)

        dfs(root)
        return res