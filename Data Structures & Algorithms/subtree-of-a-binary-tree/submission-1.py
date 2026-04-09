# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None: return True
        elif root is None or subRoot is None:  return False
        
        def check(r: TreeNode, s: TreeNode) ->bool:
            if r is None and s is None: return True
            elif r is None or s is None:  return False
            if r.val != s.val: return False
            return check(r.left, s.left) and check(r.right,s.right) 
        checked = False
        if root.val == subRoot.val:
            checked = check(root, subRoot)

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or checked

        