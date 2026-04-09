class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1, res = 0;
        while (l < r) {
            res = max(min(heights[l], heights[r]) * (r-l), res);
            if (heights[l] < heights[r]) l += 1;
            else r -= 1;
        }
        return res;
    }
};
