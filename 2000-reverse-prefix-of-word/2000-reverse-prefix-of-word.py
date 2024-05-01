class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        lst = list(word)
        for i, c in enumerate(lst):
            if c == ch:
                self.reverse(lst, 0, i)
                break
        return ''.join(lst)
    
    def reverse(self, lst, l, r):
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1