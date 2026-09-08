# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
        indices = {val : idx for idx, val in enumerate(inorder)}

        pre_idx = 0 # index of the root in the preorder list, initialized to 0

        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return 
            
            root = TreeNode(preorder[pre_idx])
            pre_idx += 1
            idx = indices[root.val]
            root.left = dfs(l, idx-1)
            root.right = dfs(idx+1, r)

            return root

        return dfs(0, len(preorder) - 1)

        