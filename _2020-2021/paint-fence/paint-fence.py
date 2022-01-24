class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0
        if n == 1: return k
        # diff[i-1] -> 2 choices: same[i] or diff[i]
        # same[i-1] -> 1 choice: diff[i] only
        # => same[i] = diff[i-1]
        # diff[i] = diff[i-1]*(k-1) + same[i-1]*(k-1)
        same, diff = k, k*(k-1)
        for i in range(3, n+1):
            same, diff = diff, (diff + same)*(k-1) 
        return same + diff
            