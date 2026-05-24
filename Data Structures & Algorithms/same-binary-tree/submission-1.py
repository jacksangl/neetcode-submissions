# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        

        p_vals, q_vals = [], []
        def traverse(node, arr):
            if node is None:
                arr.append(None)
                return
            
            arr.append(node.val)
            
            traverse(node.left, arr)
            traverse(node.right, arr)
            

        traverse(p, p_vals)
        traverse(q, q_vals)
        return p_vals == q_vals