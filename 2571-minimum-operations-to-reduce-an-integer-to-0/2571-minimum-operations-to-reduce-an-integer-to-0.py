class Solution:
    def minOperations(self, n: int) -> int:
        #greedy: find the closest smaller and larger powers of 2
        #then find the min distance to them
        if n <= 1: return n
        nextLarger = 1
        while nextLarger < n:
            nextLarger *= 2
        prevSmaller = nextLarger//2
        return 1 + min(self.minOperations(nextLarger - n), self.minOperations(n - prevSmaller))