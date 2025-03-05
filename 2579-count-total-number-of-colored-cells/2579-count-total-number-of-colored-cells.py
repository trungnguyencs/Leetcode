class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 5
        ans = 5
        for i in range(3, n + 1):
            ans += 4 * i - 4 #4 boundary diagonals (length n each) overlap 4 cells total
        return ans