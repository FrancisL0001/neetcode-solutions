# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.left and root.right:
            return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        elif not root.left:
            return 1 + self.maxDepth(root.right)
        elif not root.right:
            return 1 + self.maxDepth(root.left)
        else:
            return 1