# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def dfs(node, max_seen):
            nonlocal res
            if node is None:
                return
            
            if node.val >= max_seen:
                res += 1
            max_seen = max(node.val, max_seen)

            dfs(node.left, max_seen)
            dfs(node.right, max_seen)
        dfs(root, root.val)
        return res