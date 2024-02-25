class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        mcount = 0
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = []
            dic[num].append(i)
            mcount = max(len(dic[num]), mcount)
        ans = len(nums)
        for num in dic:
            if len(dic[num]) == mcount:
                ans = min(ans, max(dic[num]) - min(dic[num]) + 1)
        return ans