class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        dic = {}
        for r, num in enumerate(nums):
            dic[num] = r
            tmpDic = deepcopy(dic)
            for prevNum, i in tmpDic.items(): #TreeMap will give better runtime
                if abs(num - prevNum) > 2:
                    l = max(l, i + 1)
                    del dic[prevNum]
            ans += r - l + 1
        return ans