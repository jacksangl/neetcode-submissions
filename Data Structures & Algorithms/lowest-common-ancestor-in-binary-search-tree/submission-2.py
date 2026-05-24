# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        low, high = min(p.val, q.val), max(p.val, q.val)

        def check(node):
            value = node.val
            if low < value and high < value:
                return check(node.left)
            elif low > value and high > value:
                return check(node.right)
            else:
                return node
        return check(root)
                
        
