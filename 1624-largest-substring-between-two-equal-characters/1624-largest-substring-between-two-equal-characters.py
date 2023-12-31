class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstIdx = {}
        maxDistance = -1
        for i, ch in enumerate(s):
            if ch not in firstIdx:
                firstIdx[ch] = i
            else:
                maxDistance = max(maxDistance, i - firstIdx[ch] - 1)
        return maxDistance