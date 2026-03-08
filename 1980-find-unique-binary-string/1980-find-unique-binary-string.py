class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        self.nums = set(nums)
        return self.backtrack([], 0, n)

    def backtrack(self, arr, i , n):
        if i == n:
            s = ''.join(arr)
            if s not in self.nums: return s
            return
        for ch in '01':
            s = self.backtrack(arr + [ch], i + 1, n)
            if s: return s