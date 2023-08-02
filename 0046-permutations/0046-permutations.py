class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack([], nums)
        return self.ans
    
    def backtrack(self, arr, nums):
        if len(arr) == len(nums):
            self.ans.append(arr[:])
            return
        for num in nums:
            if num not in arr:
                self.backtrack(arr + [num], nums)