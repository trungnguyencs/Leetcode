class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0
        for i, ch in enumerate(s):
            if ch != ' ' and (i == 0 or s[i-1] == ' '):
                segments += 1
        return segments
                
                