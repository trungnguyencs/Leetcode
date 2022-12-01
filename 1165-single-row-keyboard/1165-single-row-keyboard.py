class Solution:
    def calculateTime(self, keyboard: str, s: str) -> int:
        d = {ch: i for i, ch in enumerate(keyboard)}
        return d[s[0]] + sum(abs(d[s[i+1]] - d[s[i]]) for i in range(len(s) - 1))