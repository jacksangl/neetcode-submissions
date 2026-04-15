class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 1) {
            if (nums[0] == target) return 0;
            return -1;
        }

        int l = 0, r = nums.size()-1;

        // find pivot. then binary search the pivot side

        while (l < r) {
            int middle = l + (r-l) / 2;

            if (nums[r] < nums[middle]) l = middle + 1;
            else r = middle;
        }
        int pivot = l;

        // now that we found the pivot at l we can figure out which side its on
        l = 0, r = nums.size()-1;
        // the side we have to search is the side if nums[r] >= target
        // otherwise its on the other side
        if (nums[r] >= target) l = pivot;
        else r = pivot - 1;

        while (l <= r) {
            int middle = l + (r - l) / 2;

            if (nums[middle] == target) return middle;
            else if (nums[middle] > target) r = middle-1;
            else l = middle+1;
        }




        return -1;
    }
};
