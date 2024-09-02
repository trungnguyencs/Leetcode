class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        oneRound = sum(chalk)
        k %= oneRound
        for i, num in enumerate(chalk):
            k -= num
            if k < 0: return i
        return 0