class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack(nums, [], set())
        return self.ans
    
    def backtrack(self, nums, arr, visited):
        if len(arr) == len(nums):
            self.ans.append(arr[:])
            return
        for i, num in enumerate(nums):
            if i in visited: continue
            arr.append(nums[i]); visited.add(i)
            self.backtrack(nums, arr, visited)
            arr.pop(); visited.remove(i)