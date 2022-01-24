class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        isPrime = [True]*n
        isPrime[0], isPrime[1] = False, False
        for i in range(2, n//2 + 1):
            if isPrime[i]:
                for j in range(2, (n-1)//i + 1):
                    isPrime[i*j] = False 
        return sum(isPrime)