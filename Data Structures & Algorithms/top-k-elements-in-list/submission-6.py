class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        length = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            length[value].append(key)
        res = []
        for i in range (len(length) -1, -1, -1):
            for num in length[i]:
                res.append(num)
                if len(res) >= k:
                    return res

        return res