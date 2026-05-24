# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        nodes = {}
        def dfs(node):
            if not node:
                return 0
            elif node in nodes:
                return nodes[node]
            if node.left not in nodes or node.right not in nodes:
                nodes[node.left] = dfs(node.left)
                nodes[node.right] = dfs(node.right)
            
            nodes[node] = 1 + max(nodes[node.left], nodes[node.right])
            return nodes[node]

        def run(node):
            if not node:
                return 0
            cur = dfs(node.left) + dfs(node.right)
            return max(cur, run(node.left), run(node.right))
        
        return run(root)