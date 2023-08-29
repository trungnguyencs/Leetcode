class Solution:
    # # 2 passes: find minimum penalty
    # def bestClosingTime(self, s: str) -> int:
    #     totalY = s.count('Y')
    #     totalN = len(s) - totalY
    #     curY, curN = 0, totalN
    #     minPenalty, ans = len(s), 0
    #     for i, c in enumerate(s):
    #         if c == 'Y':
    #             curY += 1
    #         else:
    #             curN += 1
    #         if curN + (totalY - curY) < minPenalty:
    #             minPenalty = curN + (totalY - curY)
    #             ans = i + 1
    #     return ans
    
    # 1 pass: find maximum profit
    def bestClosingTime(self, s: str) -> int:
        profit = maxProfit = ans = 0
        for i, c in enumerate(s):
            profit += (1 if c == 'Y' else -1)
            if profit > maxProfit:
                maxProfit = profit
                ans = i + 1
        return ans