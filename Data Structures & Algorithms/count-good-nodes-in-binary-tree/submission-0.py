# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, curMax):
            if not node:
                return 0

            if node.val < curMax:
                return dfs(node.left, curMax) + dfs(node.right, curMax)
            else:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)

        res = dfs(root, -1 * float("inf"))

        return res


    # go depth first and at each level pass a current max, the current maximum along this path
    # then check if the value of the current node is greater than the current max, meaning 
    # all nodes along this path are less than this node so it's a good node
    # the rval will be the sum of the good nodes on the left, those on the right and whether the current one is a good node or not