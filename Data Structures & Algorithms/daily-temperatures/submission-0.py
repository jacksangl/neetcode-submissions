class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # brute force
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
            
        return res