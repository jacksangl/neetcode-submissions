class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        total = 1
        res = []
        zeros = 0

        for num in nums:
            if num == 0 and zeros < 1:
                zeros += 1
                continue
            total *= num
        if zeros >= 2:
            return [0] * len(nums)
        if zeros == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(0) 
                else:
                    res.append(total)
            return res

        for num in nums:
                res.append(int(total/num))
        return res