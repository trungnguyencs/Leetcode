class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #idea is from 370. Range Addition
        rangeAddition = [0]*(len(nums) + 1)
        for s, e in queries:
            rangeAddition[s] += 1
            rangeAddition[e + 1] -= 1
        cur = 0
        for i in range(len(nums)):
            cur += rangeAddition[i]
            if cur < nums[i]: return False
        return True