class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: return 1/self.myPow(x, -n)
        if n == 0: return 1
        tmp = self.myPow(x, n//2)
        return tmp*tmp if n % 2 == 0 else tmp*tmp*x