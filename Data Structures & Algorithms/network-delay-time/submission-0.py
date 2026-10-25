from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = {i: [] for i in range(1, n+1)}
        for ui, vi, ti in times:
            nodes[ui].append((vi,ti))

        distances = {node: float('inf') for node in nodes}
        distances[k] = 0
        q = deque([k])

        while q:
            node = q.popleft()
            for child, cost in nodes[node]:
                if distances[node] + cost < distances[child]:
                    distances[child] = distances[node] + cost
                    q.append(child)

            
        res = max(distances.values())
        return res if res != float('inf') else -1


        
