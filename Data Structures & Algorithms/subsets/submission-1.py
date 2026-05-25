class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        length = len(nums)
        seen = set()
        def find(cur, idx, take):
            if tuple(cur) not in seen and idx == length:
                seen.add(tuple(cur))
                res.append(cur)
                return
            elif idx == length: return
            if take: cur = cur + [nums[idx]]

            find(cur, idx+1, False)
            find(cur, idx+1, True)

        find([], -1, False)

        return res
