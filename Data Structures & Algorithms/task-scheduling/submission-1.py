class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        maxHeap = [[-freq, task] for task, freq in counts.items()]
        heapq.heapify(maxHeap)
        used = []
        res = 0
       
        while maxHeap:
            for i in range(n+1):
                if not maxHeap and used:
                    res += n+1-i
                    break
                elif not maxHeap:
                    break
                freq, char = heapq.heappop(maxHeap)
                freq = -freq - 1
                res += 1
                if freq != 0:
                    heapq.heappush(used, [-freq, char])
            
            while used:
                freq, char = heapq.heappop(used)
                heapq.heappush(maxHeap, [freq, char])
            
        return res
