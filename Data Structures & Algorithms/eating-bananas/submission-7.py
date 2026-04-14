from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)

        res = piles[-1]

        l, r = 1, piles[-1]
        
        while l <= r:
            m = (l+r) // 2
            curr = 0
            for num in piles:
                curr += (ceil(num / m))
            if curr > h:
                l = m + 1
            else:
                r = m - 1
        
            
        return l


        # maxxi = 4
        # [4, 3, 2, 1]
        # l = 0, r = 4
        # m = 2
        # for num in piles
        #   while 4 > 0
        #       4 = 4-2
        #       curr + 1
        #   cur = 2
        # while 3 > 0
        # cur = 4
        # cur = 6
        # 



        # brute force 
        '''
        for i in range(maxi, 0, -1):
            curr = 0
            for num in piles:
                if curr >= h:
                    return i+1
                while num > 0:
                    num -= i
                    curr += 1
        '''
