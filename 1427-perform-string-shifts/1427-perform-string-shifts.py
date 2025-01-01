class Solution:
    def stringShift(self, s: str, shifts: List[List[int]]) -> str:
        totalShift = 0
        for d, shift in shifts:
            totalShift += shift if d == 1 else -shift
        totalShift %= len(s)
        s = list(s)
        self.reverse(s, 0, len(s) - 1)
        self.reverse(s, 0, totalShift - 1)
        self.reverse(s, totalShift, len(s) - 1)
        return ''.join(s)
        
    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1