class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counterS, counterT = Counter(s), Counter(t)
        ans = 0
        for ch, countS in counterS.items():
            ans += max(0, countS - counterT[ch]) 
        return ans