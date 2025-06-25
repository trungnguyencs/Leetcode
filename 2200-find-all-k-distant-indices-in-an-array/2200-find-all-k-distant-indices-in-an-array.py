class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        last = -1
        for i, num in enumerate(nums):
            if num == key:
                l = max(last + 1, i - k)
                r = min(len(nums) - 1, i + k)
                ans.extend(range(l, r + 1))
                last = r
        return ans