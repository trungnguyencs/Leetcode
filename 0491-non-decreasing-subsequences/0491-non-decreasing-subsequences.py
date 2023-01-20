class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        self.backtrack(nums, 0, [])
        return self.ans
        
    def backtrack(self, nums, i, arr):
        if i == len(nums):
            if len(arr) >= 2:
                self.ans.add(tuple(arr))
            return
        if not arr or nums[i] >= arr[-1]:
            self.backtrack(nums, i+1, arr+[nums[i]])
        self.backtrack(nums, i+1, arr)