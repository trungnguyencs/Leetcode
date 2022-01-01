class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for k in counter:
            if k + 1 in counter:
                ans = max(ans, counter[k] + counter[k+1])
        return ans