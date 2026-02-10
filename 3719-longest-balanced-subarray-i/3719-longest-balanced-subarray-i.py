class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            oddSet, evenSet = set(), set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    evenSet.add(nums[j])
                else:
                    oddSet.add(nums[j])
                if len(oddSet) == len(evenSet):
                    ans = max(ans, j - i + 1)
        return ans