class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # s(1) = 0
        # s(2) = 01
        # s(3) = 0110
        # s(4) = 01101001
        # => pattern will be like:
        # s(n) = s(n-1) + reversed(s(n-1))
        # => algo: see if kth in in the first half or second half of s(n)
        # if first half => same as kth in s(n-1), else: flipped of kth - length//2 in s(n-1)
        if n == 1: return 0
        length = 2**(n - 1)
        if k <= length//2:
            return self.kthGrammar(n - 1, k)
        return 1 - self.kthGrammar(n - 1, k - length//2)