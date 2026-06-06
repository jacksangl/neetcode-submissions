class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        seen = set()

        nodes = {}
        res = 0
        for i in range(n): nodes[i] = []

        for parent, child in edges:
            nodes[parent].append(child)
            nodes[child].append(parent)
        

        def dfs(node, prev, visited):
            if node in visited or node == prev or node in seen:
                return
            
            visited.add(node)
            # child = 1 nodes = {0: [1], 1: [0,2], ...}
            for child in nodes[node]:
                dfs(child, node, visited)
            visited.remove(node)
            seen.add(node)
            return

        
        for i in range(n):
            if i not in seen:
                dfs(i, -1, set())
                res += 1
        return res
