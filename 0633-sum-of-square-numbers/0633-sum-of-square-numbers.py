class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = {x**2 for x in range(int(c**0.5) + 1)}
        return any(c - square in squares for square in squares)
            