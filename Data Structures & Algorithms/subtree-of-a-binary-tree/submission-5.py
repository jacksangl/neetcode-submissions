# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return root == subRoot
        def check_subroot(node, arr):
            if not node:
                arr.append(None)
                return
            

            arr.append(node.val)

            check_subroot(node.left, arr)
            check_subroot(node.right, arr)
        
        subRoot_arr = []
        check_subroot(subRoot,subRoot_arr)
        
        queue = deque()
        queue.append(root)
        check_arr = []

        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                
                if node and node.val == subRoot.val:
                    check_subroot(node, check_arr)

                    if check_arr == subRoot_arr:
                        return True
                    check_arr = []
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return False

