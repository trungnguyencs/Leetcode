class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # x + minDelta >= lower and x + maxDelta <= upper
        # -> x >= lower - minDelta and x <= upper - maxDelta
        # -> #x = upper - maxDelta - (lower - minDelta) + 1
        m = M = delta = 0
        for d in differences:
            delta += d
            m = min(m, delta)
            M = max(M, delta)
        return max(0, upper - M - (lower - m) + 1)