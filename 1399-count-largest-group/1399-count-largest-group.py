class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = [0]*37
        for num in range(1, n + 1):
            sumDigits = self.sumDigits(num)
            counter[sumDigits] += 1
        maxFreq = max(counter)
        return len([freq for freq in counter if freq == maxFreq])

    def sumDigits(self, num):
        ans = 0
        while num:
            ans += num % 10
            num //= 10
        return ans