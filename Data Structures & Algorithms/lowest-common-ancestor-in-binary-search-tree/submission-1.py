# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        low, high = min(p.val, q.val), max(p.val, q.val)

        queue = deque()
        queue.append(root)

        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                value = node.val

                # cases
                # case low < value and high > value this is the LCA

                if low <= value and value <= high:
                    return node
                
        
