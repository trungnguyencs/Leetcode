class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = 0
        for ch in s:
            d = ord(ch) - ord('a') + 1
            num += (d if d < 10 else d//10 + d % 10)
        for _ in range(k - 1):
            tmp = 0
            while num:
                tmp += num % 10
                num //= 10
            num = tmp
        return num