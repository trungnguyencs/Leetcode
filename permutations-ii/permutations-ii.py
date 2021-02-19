class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        self.backtrack(nums, [], set())
        return self.ans
    
    def backtrack(self, nums, arr, visited):
        if len(arr) == len(nums):
            self.ans.add(tuple(arr[:]))
            return
        for i, num in enumerate(nums):
            if i in visited: continue
            arr.append(nums[i]); visited.add(i)
            self.backtrack(nums, arr, visited)
            arr.pop(); visited.remove(i)