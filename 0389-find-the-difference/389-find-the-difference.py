class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterS, counterT = Counter(s), Counter(t)
        for k, v in counterT.items():
            if k not in counterS or v > counterS[k]:
                return k