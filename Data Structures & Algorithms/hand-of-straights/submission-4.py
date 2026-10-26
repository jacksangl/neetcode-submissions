class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        
        hand.sort()

        heap = []

        for h in hand:
            if heap and heap[0][0] == h-1:
                _, length = heapq.heappop(heap)
                if length+1 == groupSize:
                    continue
                heapq.heappush(heap, (h, length+1))
            else:
                heapq.heappush(heap, (h, 1))
        
        return True if not heap else False
            

"""
heap = [(-2,2), (-2,1)
"""
