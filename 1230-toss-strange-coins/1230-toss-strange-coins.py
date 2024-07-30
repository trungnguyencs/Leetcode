class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        @cache
        def dp(i, headCount):
            if len(prob) - i < headCount: return 0
            if i == len(prob): return 1
            if headCount == 0:
                return (1 - prob[i]) * dp(i+1, 0)
            return prob[i] * dp(i+1, headCount - 1) + (1 - prob[i]) * dp(i+1, headCount)
        
        return dp(0, target)