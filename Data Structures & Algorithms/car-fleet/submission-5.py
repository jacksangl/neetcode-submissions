class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        values = [[position[i],speed[i]] for i in range(len(speed))]
    
        values = sorted(values, reverse=True)
        # okay now the setup is done
        stack = []
        for pos, speed in values:
            time = (target-pos) / speed
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
        return len(stack)
    
        

        
