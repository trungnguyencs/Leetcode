class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = maxA = maxAMinusB = 0
        for num in nums:
            ans = max(ans, maxAMinusB * num)
            maxAMinusB = max(maxAMinusB, maxA - num)
            maxA = max(maxA, num)
        return ans