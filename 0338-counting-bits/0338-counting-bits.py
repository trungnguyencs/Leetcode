class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i>>1] + (i & 1) # ans[i] == ans[i//2] + (i % 2)
        return ans