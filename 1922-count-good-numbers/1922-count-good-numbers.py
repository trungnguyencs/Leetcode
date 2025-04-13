class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        if n % 2 == 0:
            return self.powmod(4, n//2, MOD) * self.powmod(5, n//2, MOD) % MOD
        return self.powmod(4, n//2, MOD) * self.powmod(5, n//2, MOD) * 5 % MOD
        
    def powmod(self, x, n, mod):
        if n == 0: return 1
        if n == 1: return x % mod
        p = self.powmod(x, n//2, mod)
        if n % 2 == 0:
            return p * p % mod
        return p * p * x % mod