class Solution:
    @cache
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        minOps = n
        for i in self.getFactors(n):
            if i in [1, n]: continue
            minOps = min(minOps, n//i + self.minSteps(i))
        return minOps
        
    def getFactors(self, n):
        factors = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n//i)
        return factors