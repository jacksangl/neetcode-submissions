class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        '''# brute force
        res = []
        for i in range(len(temperatures)):
            appended = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    appended = True
                    res.append(j-i)
                    break
            if not appended:
                res.append(0)
            
        return res'''
        

        # optimal sltn

        res = [0] * len(temperatures)
        heap = []
        for i in range(len(temperatures)):
            day = (temperatures[i], i)
            heapq.heappush(heap, day)
            while day[0] != heap[0][0]:
                val = heapq.heappop(heap)
                i_val = val[1]
                res[i_val] = i - i_val
        
        return res
            
            