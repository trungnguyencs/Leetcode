class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        #key point is getting the list of prime numbers between left and right, see 204. Count Primes
        primes = self.sieve(left, right)
        ans = [-1, -1]
        minDiff = float('inf')
        for i in range(len(primes) - 1):
            diff = primes[i+1] - primes[i]
            if diff < minDiff:
                minDiff = diff
                ans = [primes[i], primes[i+1]]
        return ans

    def sieve(self, lowerLimit, upperLimit):
        isPrime = [True]*(upperLimit + 1)
        isPrime[0] = isPrime[1] = False
        for num in range(2, int(upperLimit**0.5) + 1):
            if isPrime[num]:
                for multiplier in range(2, upperLimit//num + 1):
                    isPrime[num * multiplier] = False
        return [num for num, prime in enumerate(isPrime) if prime and num >= lowerLimit]