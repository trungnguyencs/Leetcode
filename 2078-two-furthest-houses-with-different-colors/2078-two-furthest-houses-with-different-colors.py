class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l, r = 0, len(colors) - 1
        while l <= r:
            if colors[l] != colors[-1]:
                return len(colors) - 1 - l
            if colors[r] != colors[0]:
                return r
            l += 1
            r -= 1
        return len(colors) - 1