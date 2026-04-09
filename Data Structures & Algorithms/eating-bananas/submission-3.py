class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # non optimal
        
        # optimal
        l, r, = 1 , max(piles)
        minimum = r
        while l <= r:
            hours = h
            m = (l+r) // 2
            for num in piles:
                total = math.ceil(num/m)
                hours -= total
            if hours >= 0:
                r = m - 1
                minimum = min(minimum, m)
            elif hours < 0:
                l = m + 1
        return minimum
            
                