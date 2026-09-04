# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        def dfs(roots):
            if not roots:
                return []
            
            left = dfs(roots.left)
            right = dfs(roots.right)

            res = [[roots.val]]

            while left and right:
                l = left.pop(0)
                r = right.pop(0)

                res.append(l + r)

            if left:
                res.extend(left)

            if right:
                res.extend(right)

            return res

        return dfs(root)