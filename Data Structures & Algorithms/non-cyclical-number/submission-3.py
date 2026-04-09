class Solution:
    def isHappy(self, n: int) -> bool:
        
        # sum of the squares of its digits
        # repeat until number == 1
        cache = set()
        
        def check(n):
            res = 0
            step = 1
            while n:
                res += ((n % 10)**2)
                n = n // (10)
                step += 1
            return res
        
        while True:
            res = check(n)
            if res == 1:
                return True
            elif res in cache:
                return False
            cache.add(res)
            n = res
