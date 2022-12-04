class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        leftSum, total = 0, sum(nums)
        ans, minAveDiff = 0, float('inf')
        for i, num in enumerate(nums):
            leftSum += num
            rightSum = total - leftSum
            aveDiff = abs(leftSum//(i + 1)) if i == len(nums) - 1 else abs(leftSum//(i + 1) - rightSum//(len(nums) - i - 1))
            if aveDiff < minAveDiff:
                ans, minAveDiff = i, aveDiff
        return ans