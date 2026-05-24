# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, maxi, mini):
            if node is None:
                return True
            
            if node.val >= maxi or node.val <= mini:
                return False
            if (node.left and node.left.val >= node.val) or (node.right and node.right.val <= node.val): 
                return False
            
            return dfs(node.left, min(maxi, node.val), mini) and dfs(node.right, maxi, max(mini, node.val))
        return dfs(root, float('inf'), -float('inf'))