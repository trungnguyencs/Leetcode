class Solution:
    def numSquares(self, n: int) -> int:
        self.squares = {x**2 for x in range(1, 101)}
        return self.dp(n)
    
    @cache    
    def dp(self, n):
        if n in self.squares: return 1
        return min(1 + self.dp(n - x) for x in self.squares if n > x)