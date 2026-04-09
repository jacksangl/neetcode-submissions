class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        res = []
        for num, count in counts.items():
            heapq.heappush(heap, (-count, num))
        while heap and k > 0:
            key = heapq.heappop(heap)
            res.append(key[1])
            k -= 1
        return res
