class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        cache = {} 
        res = []
        for num in nums:
            cache[num] = cache.get(num, 0) + 1
        
        for key, value in cache.items():
            if len(heap) < k:
                heapq.heappush(heap, [value, key])
            elif value > heap[0][0]:
                heapq.heapreplace(heap, [value, key])
        for value in heap:
            res.append(value[1])
        return res
