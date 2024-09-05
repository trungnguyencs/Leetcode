class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missingSum = mean * (n + len(rolls)) - sum(rolls)
        if not n <= missingSum <= 6*n: return []
        ans = [missingSum//n]*n
        for i in range(missingSum % n):
            ans[i] += 1
        return ans