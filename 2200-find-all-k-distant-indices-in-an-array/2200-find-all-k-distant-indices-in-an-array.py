class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = set()
        for i, num in enumerate(nums):
            if num == key:
                ans.update(range(max(0, i - k), 1 + min(len(nums) - 1, i + k)))
        return sorted(list(ans))