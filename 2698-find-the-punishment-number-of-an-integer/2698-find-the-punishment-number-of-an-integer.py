class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            sq = i * i
            if self.backtrack(sq, i):
                ans += sq
        return ans

    def backtrack(self, num, target):
        if num < target: return False
        if num == target: return True
        for i in range(1, len(str(num))):
            if self.backtrack(num//(10**i), target - num % (10**i)):
                return True
        return False