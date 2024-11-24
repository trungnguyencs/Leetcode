class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        #If we have a zero anywhere we can use it to flip all negatives into positives
        #If we have even number of negatives, we can turn all negatives into positives
        #Otherwise, we turn the smallest absolute value into a negative, and everything else - into positives
        zeroCount = negCount = sumVal = 0
        smallestAbs = float('inf')
        for row in matrix:
            for num in row:
                zeroCount += num == 0
                negCount += num < 0
                smallestAbs = min(smallestAbs, abs(num))
                sumVal += abs(num)
        return sumVal if zeroCount > 0 or negCount % 2 == 0 else sumVal - 2*smallestAbs