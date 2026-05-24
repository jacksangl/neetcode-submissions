# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def bfs(root, arr):
            queue = deque()
            queue.append(root)
            while queue:
                length = len(queue)
                for _ in range(length):
                    node = queue.popleft()
                    if node:
                        queue.append(node.left)
                        queue.append(node.right)
                        arr.append(node.val)
                    else: arr.append(None)
            return arr

        p_vals = bfs(p, [])
        q_vals = bfs(q, [])
        print(p_vals)
        print(q_vals)
        return p_vals == q_vals

        

