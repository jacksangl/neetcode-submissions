class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;

        while (l < r) {
            auto total = nums[l] + nums[r];

            if (total < target) l+=1;
            else if (total > target) r-=1;
            else return {l+1, r+1};
        }
    }
};
