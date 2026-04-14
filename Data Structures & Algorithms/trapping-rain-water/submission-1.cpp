class Solution {
public:
    int trap(vector<int>& height) {
        int length = height.size();
        vector <int> max_r(length+2, 0);
        vector <int> max_l(length+2, 0);
        int res = 0;

        for (int i = 0; i < length; i++) max_l[i+1] = max(max_l[i], height[i]);
        for (int i = length; i > 0; i--) max_r[i] = max(max_r[i+1], height[i-1]);

        for (int i = 0; i < length; i++) res += min(max_l[i+1], max_r[i+1]) - height[i];
        return res;
    }
};
