class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # precompute leftSum[i]: sum of elements before nums[i] and rightSum[i]: sum of elements after nums[i]
        # => ans[i] = num*i - leftSum[i] + rightSum[i] - num*(n - i - 1)
        n = len(nums)
        leftSum = [0]*n
        rightSum = [0]*n
        ans = []
        s = 0
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
        for i, num in enumerate(nums):
            if i != 0:
                leftSum[i] = leftSum[i-1] + nums[i-1]
            ans.append(num*i - leftSum[i] + rightSum[i] - num*(n - i - 1))
        return ans