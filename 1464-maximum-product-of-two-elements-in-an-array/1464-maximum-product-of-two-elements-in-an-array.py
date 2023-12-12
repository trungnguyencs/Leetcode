class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        M = secondM = float('-inf')
        for num in nums:
            if num > M:
                M, secondM = num, M
            elif num > secondM:
                secondM = num
        return (M - 1)*(secondM - 1)