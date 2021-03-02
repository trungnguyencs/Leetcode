class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack(nums, [], 0)
        return self.ans
        
    def backtrack(self, nums, arr, i):
        if i == len(nums):
            self.ans.append(arr[:])
            return
        self.backtrack(nums, arr, i+1)
        self.backtrack(nums, arr + [nums[i]], i+1)