class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        suffixSum = piles
        for i in range(len(suffixSum) - 2, -1, -1):
            suffixSum[i] += suffixSum[i+1]
        
        @cache
        def dp(i, m):
            if i >= len(piles): return 0
            maxPoints = 0
            for x in range(1, min(2*m, len(piles) - i) + 1):
                M = max(m, x)
                maxPoints = max(maxPoints, suffixSum[i] - dp(i + x, M))
            return maxPoints
        
        return dp(0, 1)