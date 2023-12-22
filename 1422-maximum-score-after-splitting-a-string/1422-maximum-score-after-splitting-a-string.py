class Solution:
    def maxScore(self, s: str) -> int:
        totalOneCount = s.count('1')
        leftZeroCount = maxScore = 0   
        for i in range(len(s) - 1): #till len(s) - 1 because right string cannot be empty
            leftZeroCount += s[i] == '0'
            rightOneCount = totalOneCount - (i + 1 - leftZeroCount)
            maxScore = max(maxScore, leftZeroCount + rightOneCount)
        return maxScore