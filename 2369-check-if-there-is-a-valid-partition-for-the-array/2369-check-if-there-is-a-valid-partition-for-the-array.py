class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        if len(nums) == 2: return nums[0] == nums[1]
        dp = [False]*len(nums)
        if nums[0] == nums[1]:
            dp[1] = True
        if nums[0] == nums[1] == nums[2]:
            dp[2] = True
        if nums[2] - nums[1] == nums[1] - nums[0] == 1:
            dp[2] = True
        for i in range(3, len(dp)):
            if nums[i] == nums[i-1] and dp[i-2]:
                dp[i] = True
            if nums[i] == nums[i-1] == nums[i-2] and dp[i-3]:
                dp[i] = True
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2] == 1 and dp[i-3]:
                dp[i] = True
        return dp[-1]