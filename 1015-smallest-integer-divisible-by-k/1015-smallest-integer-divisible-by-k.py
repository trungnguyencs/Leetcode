class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0: return -1
        # fact: 11..1 (n digits) % k == 11..1 (2n digits) % k
        # therefore, if all (1, 11, ... , 11..1 (k digits) % k != 0) then there's no such number
        num = 0
        for i in range(1, k + 1):
            num = num * 10 + 1
            if num % k == 0:
                return i
        return -1