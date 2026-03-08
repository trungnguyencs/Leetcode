class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        self.nums = set(nums)
        self.ans = ''
        self.backtrack([], 0, n)
        return self.ans

    def backtrack(self, arr, i , n):
        if i == n:
            s = ''.join(arr)
            if s not in self.nums:
                self.ans = s
            return
        self.backtrack(arr + ['0'], i + 1, n)
        self.backtrack(arr + ['1'], i + 1, n)