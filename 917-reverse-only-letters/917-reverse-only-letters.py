class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if not s[l].isalpha():
                l += 1
            elif not s[r].isalpha():
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)