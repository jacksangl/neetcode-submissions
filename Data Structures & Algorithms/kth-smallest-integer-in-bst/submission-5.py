# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        nums = []

        def preorder(node):

            if node is None:
                return
            
            preorder(node.left)
            nums.append(node.val)
            preorder(node.right)

        preorder(root)

        return nums[k-1]