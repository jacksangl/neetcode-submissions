class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force sort array and check longest subsequence
        # O(nlogn)
        if nums == []:
            return 0
        hashset = {}
       
        length, max_length = 1, 1

        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset[nums[i]] = i

        for key in hashset:
            if key-1 not in hashset:
                num = key+1
                while num in hashset:
                    length += 1
                    num += 1
                max_length = max(length, max_length)
                length = 1
            
            

                
            
           

        return max_length