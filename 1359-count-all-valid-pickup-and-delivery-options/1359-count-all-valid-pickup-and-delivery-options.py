class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        # assume already have i pairs inserted, now insert 1 more pair
        # we can see first pole has 2n + 1 slots, second pole has 2n + 2 slots
        # but first pole must go before second pole -> total (2n + 1)*(2n + 2)//2*f(i) choices
        for i in range(1, n):
            ans = ans*(2*i + 1)*(2*i + 2)//2 % (10**9 + 7)
        return ans