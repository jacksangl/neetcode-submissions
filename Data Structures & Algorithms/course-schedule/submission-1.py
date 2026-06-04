class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}

    def add(self, child: Node):
        self.children[child.val] = child

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        nodes = {}
        
        for nxt, prev in prerequisites:
            if nxt not in nodes:
                nodes[nxt] = Node(nxt)
            if prev not in nodes:
                nodes[prev] = Node(prev)
                

            nodes[prev].add(nodes[nxt])
        
        def dfs(node, visited = set()):
            if node.val in visited: return False
            visited.add(node.val)
            for child in node.children.values():
                if not dfs(child, visited):
                    return False
            visited.remove(node.val)
            return True
                


        print(*nodes)        
        for node in nodes.values():
            visited = set()
            if not dfs(node, visited):
                return False
        return True
        


