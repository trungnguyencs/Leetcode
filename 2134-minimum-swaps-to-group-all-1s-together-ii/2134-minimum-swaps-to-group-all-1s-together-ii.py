class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # sliding window of size nums.count(1)
        oneCount = nums.count(1)
        window = maxWindow = 0
        circledNums = nums + nums
        for i, num in enumerate(circledNums):
            if num == 1:
                window += 1
            if i >= oneCount:
                window -= circledNums[i - oneCount]
            maxWindow = max(maxWindow, window)
        return oneCount - maxWindow