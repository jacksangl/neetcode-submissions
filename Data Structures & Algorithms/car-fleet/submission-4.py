class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p, s] for p,s in zip(position,speed)]
        res = []

        for p, s in sorted(pair)[::-1]:
            time_arrive = (target - p)/ s
            if not res or time_arrive > res[-1]:
                res.append(time_arrive)
    
        return len(res)