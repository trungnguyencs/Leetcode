class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min = secondMin = float('inf')
        max = secondMax = float('-inf')
        for num in nums:
            if num >= max:
                max, secondMax = num, max
            elif num > secondMax:
                secondMax = num
            if num <= min:
                min, secondMin = num, min
            elif num < secondMin:
                secondMin = num
        return max*secondMax - min*secondMin