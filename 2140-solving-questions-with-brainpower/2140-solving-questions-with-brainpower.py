class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(questions): return 0
            point, skip = questions[i]
            return max(dp(i + 1), point + dp(i + skip + 1))
        return dp(0)