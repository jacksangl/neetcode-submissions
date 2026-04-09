#include <algorithm>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        unordered_set <int> cache (nums.begin(), nums.end());
        auto res = 1;
        for (auto num: nums) {
            cache.insert(num);
        }
        for (auto num : nums) {
            if (!cache.contains(num - 1)){
                auto cur = num;
                while (cache.contains(cur)) {
                    res = max(res, cur-num + 1);
                    cur += 1;
                }
            }
        }
        return res;
    }
};
