# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or (root.left is None and root.right is None): return root
        node = root
        def dfs(cur):
            if cur is None: return
            temp = cur.left
            cur.left = cur.right
            cur.right = temp
            dfs(cur.left)
            dfs(cur.right)
        dfs(node)
        return root

        
    