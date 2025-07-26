class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxNum = float('-inf')
        positiveSum = 0
        positiveSet = set()
        for num in nums:
            if num > 0:
                if num not in positiveSet:
                    positiveSum += num
                positiveSet.add(num)     
            maxNum = max(maxNum, num)
        return positiveSum if positiveSum > 0 else maxNum