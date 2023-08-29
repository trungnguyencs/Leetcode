class Solution:
    def bestClosingTime(self, s: str) -> int:
        totalY = s.count('Y')
        totalN = len(s) - totalY
        curY, curN = 0, totalN
        minPenalty, ans = len(s), 0
        for i, c in enumerate(s):
            if c == 'Y':
                curY += 1
            else:
                curN += 1
            if curN + (totalY - curY) < minPenalty:
                minPenalty = curN + (totalY - curY)
                ans = i + 1
        return ans