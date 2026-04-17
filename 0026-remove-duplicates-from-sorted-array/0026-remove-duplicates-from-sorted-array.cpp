class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] != nums[l]) {
                l++;
                nums[l] = nums[r];
            }
        }
        return l + 1;
    }
};