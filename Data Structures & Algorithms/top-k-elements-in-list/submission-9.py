class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = [(-freq, number) for number, freq in counts.items()]
        heapq.heapify(heap)
        res = []
        while k > 0:
            num = heapq.heappop(heap)
            res.append(num[1])
            k-= 1
        return res