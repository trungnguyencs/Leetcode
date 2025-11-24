class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        ans = []
        for num in nums:
            cur = (cur << 1) | num
            ans.append(cur % 5 == 0)
        return ans