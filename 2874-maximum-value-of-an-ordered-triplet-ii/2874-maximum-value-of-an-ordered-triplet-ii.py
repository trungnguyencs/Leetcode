class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxA = maxAMinusB = maxProd = 0
        for num in nums:
            maxProd = max(maxProd, maxAMinusB * num)
            maxAMinusB = max(maxAMinusB, maxA - num)
            maxA = max(maxA, num)
        return maxProd