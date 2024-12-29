class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        square = noSquare = 0
        ans = float('-inf')
        for num in nums:
            square = max(square + num, noSquare + num**2, num**2)
            noSquare = max(num, num + noSquare)
            ans = max(ans, square)
        return ans