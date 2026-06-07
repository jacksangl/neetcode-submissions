class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        

        n = len(intervals)
        res = []
        i = 0
      
        while i < n:
            start, end = intervals[i]
            i += 1
            while i < n:
                i_s, i_e = intervals[i]
                if i_s <= end and i_e <= end: 
                    i += 1
                    continue
                if not i_s <= end: break
                end = i_e
                i += 1
            res.append([start, end])
        
        return res
