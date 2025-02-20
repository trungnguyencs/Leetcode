class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        return self.backtrack(['']*n, 0, nums, n)

    def backtrack(self, arr, i, nums, n):
        if i == n:
            s = ''.join(arr)
            if s not in nums:
                return s
            return None
        for d in '01':
            arr[i] = d
            s = self.backtrack(arr, i + 1, nums, n)
            if s: return s