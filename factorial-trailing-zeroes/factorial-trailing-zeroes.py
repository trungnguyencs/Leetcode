class Solution:
    def trailingZeroes(self, n: int) -> int:
        # each 5 produces one trailing zero
        # each 25 produces two trailing zero
        # each 125 produces two trailing zero
        # ...
        if n == 0: return 0
        degree = int(math.log(n, 5))
        return sum([n//(5**i) for i in range(1, degree + 1)])
