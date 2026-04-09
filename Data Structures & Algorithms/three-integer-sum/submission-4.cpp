class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            int j = i+1, k = nums.size()-1;
            if (i > 0 && nums[i] == nums[i-1]) continue;
            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];
                cout << total << endl;

                if (total < 0) j += 1;
                else if (total > 0) k -= 1;
                else {
                    res.push_back({nums[i], nums[j], nums[k]});
                    j += 1;
                    k -= 1;

                    while (j < k && nums[j-1] == nums[j]) j += 1;
                    while (j < k && nums[k+1] == nums[k]) k -= 1;
                }
            }
        }
        return res;
    }
};
