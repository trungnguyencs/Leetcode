class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.ans = 0
        self.backtrack(nums, 0, [], k)
        return self.ans - 1 #exclude empty arr   
        
    def backtrack(self, nums, i, arr, k):
        if i == len(nums):
            self.ans += 1
            return
        self.backtrack(nums, i + 1, arr, k)
        if nums[i] - k not in arr:
            self.backtrack(nums, i + 1, arr + [nums[i]], k)