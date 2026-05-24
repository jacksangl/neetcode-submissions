# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()

        queue.append(root)
        levels = []
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node.val)
            
            if level: levels.append(level)
        res = []
        for level in levels:
            res.append(level[-1])
        return res