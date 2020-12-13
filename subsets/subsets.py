class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        self.backtrack(nums, 0, [])
        return self.ans
        
    def backtrack(self, nums, i, path):
        if i == len(nums): 
            return
        for j in range(i, len(nums)):
            path.append(nums[j])
            self.ans.append(path[:])
            self.backtrack(nums, j+1, path)
            path.pop()
