"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        nodes = {}
        def dfs(node, idx):
            if idx in nodes:
                return nodes[idx]
            
            nodes[idx] = Node(node.val)

            for neighbor in node.neighbors:
                n = dfs(neighbor, neighbor.val)
                if n:
                    nodes[idx].neighbors.append(n)
            return nodes[idx]
        
        return dfs(node, node.val)
