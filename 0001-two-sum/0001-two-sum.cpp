class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dic;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (dic.contains(complement)) return {i, dic[complement]};
            dic[nums[i]] = i;
        }
        return {};
    }
};