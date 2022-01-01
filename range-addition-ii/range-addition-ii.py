class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minR, minC = m, n
        for r, c in ops:
            minR = min(minR, r)
            minC = min(minC, c)
        return minR * minC