class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # prefix sum on (oneCount - zeroCount)
        diff = maxLen = 0
        dic = {0: -1}
        for i, num in enumerate(nums):
            diff += 1 if num == 1 else -1
            if diff not in dic:
                dic[diff] = i
            else:
                maxLen = max(maxLen, i - dic[diff]) # earliest index that has the same diff
        return maxLen