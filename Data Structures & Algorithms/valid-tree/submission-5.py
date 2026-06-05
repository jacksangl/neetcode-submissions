class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        if len(edges) != n-1:
            return False
        used = set()
        nodes = {}

        for i in range(n):
            nodes[i] = []
        for parent, child in edges:
            nodes[parent].append(child)
            nodes[child].append(parent)
        
        def dfs(node, prev, visited):
            if node in visited:
                return False
            if node in used:
                return True
            visited.add(node)
            for child in nodes[node]:
                print(child)
                print(prev)
                if child == prev: continue
                if not dfs(child, node, visited): return False
            used.add(node)
            visited.remove(node)
            return True
        
        return dfs(0, -1, visited = set()) and len(used) == n