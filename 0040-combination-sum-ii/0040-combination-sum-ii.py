class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.backtrack(nums, [], 0, target)
        return self.ans
        
    def backtrack(self, nums, arr, i, target):
        if target == 0:
            self.ans.append(arr[:])
            return
        if target < 0 or i == len(nums):
            return
        for j in range(i, len(nums)):
            if j != i and nums[j] == nums[j-1]: continue
            self.backtrack(nums, arr + [nums[j]], j + 1, target - nums[j])