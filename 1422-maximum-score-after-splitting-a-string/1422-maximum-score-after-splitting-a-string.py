class Solution:
    def maxScore(self, s: str) -> int:
        zeroLeft = 0
        oneRight = s.count('1')
        maxScore = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeroLeft += 1
            else:
                oneRight -= 1
            maxScore = max(maxScore, zeroLeft + oneRight)
        return maxScore