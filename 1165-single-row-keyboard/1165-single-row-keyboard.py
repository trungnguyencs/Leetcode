class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {ch: i for i, ch in enumerate(keyboard)}
        totalDistance = prev = 0
        for ch in word:
            cur = dic[ch]
            totalDistance += abs(cur - prev)
            prev = cur
        return totalDistance