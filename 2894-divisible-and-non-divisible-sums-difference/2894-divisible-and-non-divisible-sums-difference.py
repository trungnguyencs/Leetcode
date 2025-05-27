class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible = sum(x for x in range(1, n + 1) if x % m == 0)
        s = (n + 1) * n//2
        return s - 2 * divisible