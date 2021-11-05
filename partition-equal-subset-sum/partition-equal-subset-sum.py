class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1: return False
        target = s//2
        dp = [False]*(target + 1) # 2D dp matrix also works, similar to coin change
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
        return dp[-1]