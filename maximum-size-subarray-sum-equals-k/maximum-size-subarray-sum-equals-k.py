class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        s = maxLen = 0
        dic = {0: -1}
        for i, num in enumerate(nums):
            s += num
            if s - k in dic: maxLen = max(maxLen, i - dic[s-k])
            if s not in dic: dic[s] = i
        return maxLen