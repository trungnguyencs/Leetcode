class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack(nums, 0, [])
        return self.ans
        
    def backtrack(self, nums, i, arr):
        self.ans.append(arr[:])
        for j in range(i, len(nums)):
            arr.append(nums[j])
            self.backtrack(nums, j + 1, arr)
            arr.pop()