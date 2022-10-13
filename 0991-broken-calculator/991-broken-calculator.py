class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        step = 0
        while target > startValue:
            target = target//2 if target % 2 == 0 else target + 1
            step += 1
        return step + startValue - target