class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #O(n) space is trivial
        n = len(grid)
        total = n * n
        sum_val = sum(num for row in grid for num in row)
        sqr_sum = sum(num * num for row in grid for num in row)
        # Expected sum: n(n+1)/2, Expected square sum: n(n+1)(2n+1)/6
        sum_diff = sum_val - total * (total + 1) // 2
        sqr_diff = sqr_sum - total * (total + 1) * (2 * total + 1) // 6
        # Using math: If x is repeated and y is missing
        # sum_diff = x - y
        # sqr_diff = x² - y²
        repeat = (sqr_diff // sum_diff + sum_diff) // 2
        missing = (sqr_diff // sum_diff - sum_diff) // 2
        return [repeat, missing]