# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        balancedtree = True

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None: return 0
            nonlocal balancedtree 
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left-right) > 1:
                balancedtree = False
                return -1
            return max(left, right) + 1 
           

        res = dfs(root)
        return balancedtree
