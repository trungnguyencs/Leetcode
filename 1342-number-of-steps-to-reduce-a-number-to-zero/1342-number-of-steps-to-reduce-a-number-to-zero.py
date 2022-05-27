class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num:
            num = num - 1 if num & 1 else num >> 1
            step += 1
        return step