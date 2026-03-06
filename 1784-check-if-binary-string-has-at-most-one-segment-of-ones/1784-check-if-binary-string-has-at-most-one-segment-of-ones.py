class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seeZero = False
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if seeZero: return False
                seeZero = True
        return True