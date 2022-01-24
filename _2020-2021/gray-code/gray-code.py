class Solution:
    def grayCode(self, n: int) -> List[int]:
        # n == 1: [0, 1]
        # n == 2: [00, 01, 11, 10]
        # n == 3: [000, 001, 011, 010, 110, 111, 101, 100]
        # => first half of f(n) is f(n-1) adding 0 in the front
        # second half of f(n) is f(n-1) in reverse adding 1 in the front
        if n == 1: return [0, 1]
        prev = self.grayCode(n-1)
        return prev + [2**(n-1) + x for x in prev[::-1]]