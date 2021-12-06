class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddSum = evenSum = 0
        for num in position:
            if num % 2 == 0:
                evenSum += 1
            else:
                oddSum += 1
        return min(oddSum, evenSum)