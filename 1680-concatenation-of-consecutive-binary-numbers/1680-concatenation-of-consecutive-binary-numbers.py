class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        for num in range(1, n + 1):
            ans = ((ans << (len(bin(num)) - 2)) + num) % (10**9 + 7)
        return ans