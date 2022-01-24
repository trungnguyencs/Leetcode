class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0: return False
        r, x = 0, num
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        return r == num
