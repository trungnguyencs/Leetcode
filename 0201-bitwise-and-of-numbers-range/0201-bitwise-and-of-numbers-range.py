class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # m = xyz0abc
        # n = xyz1def
        # this range will include xyz0111 and xyz1000
        # which makes rangeBitwiseAnd(m, n) == xyz0000
        # => keep common bits of m & n from left to right and pad 0s to the rest
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i