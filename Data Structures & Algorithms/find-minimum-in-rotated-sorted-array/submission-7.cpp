class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size() - 1;
        if (nums[0] < nums[1] && nums[0] < nums[nums.size()-1]) return nums[0];
        while (l < r) {
            int middle = static_cast<int> ((l + r) / 2);
            if ((middle != 0 && nums[middle] < nums[middle-1])) return nums[middle];
            // case middle > r and l
            else if (nums[middle] > nums[r]) l = middle + 1;
            else r = middle - 1; 
        }
        return nums[l];
    }
};
