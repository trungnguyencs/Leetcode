class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterS, counterT = Counter(s), Counter(t)
        for ch in counterT:
            if counterT[ch] - counterS[ch] == 1: return ch
        