class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            if curSum % k not in dic:
                dic[curSum % k] = i
            elif i - dic[curSum % k] >= 2: return True
        return False