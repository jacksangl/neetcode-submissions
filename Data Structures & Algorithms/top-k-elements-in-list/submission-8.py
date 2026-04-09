class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]
        #count the frequency
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key, value in counts.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            
            for val in freq[i]:
                if len(res) == k:
                    return res
                res.append(val)
        return res