class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.backtrack(nums, [], 0)
        return self.ans
    
    def backtrack(self, nums, arr, i):
        self.ans.append(arr[:])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]: continue
            arr.append(nums[j])
            self.backtrack(nums, arr, j + 1)
            arr.pop()