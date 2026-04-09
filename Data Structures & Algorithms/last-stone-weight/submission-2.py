class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            left, right = heapq.heappop(stones), heapq.heappop(stones)
            left, right = -left, -right
            left = -(left - right)
            if -left > 0:
                heapq.heappush(stones, left)
            
        return -stones[0] if stones else 0

