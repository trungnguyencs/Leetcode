class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count = l = 0
        ans = 1
        mod = 10**9 + 7
        for r, ch in enumerate(corridor):
            if ch == 'S':
                count += 1
                if count % 2 == 0:
                    l = r
                elif count > 2:
                    ans = ans * (r - l) % mod
        return ans if (count % 2 == 0 and count != 0) else 0