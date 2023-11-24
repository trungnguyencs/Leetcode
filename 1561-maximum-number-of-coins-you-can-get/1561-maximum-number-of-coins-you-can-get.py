class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # greedy: optimal is picking the 2 largest coins and the smallest coin each time
        piles.sort(reverse=True)
        ans = 0
        n = len(piles)//3
        for i in range(1, n*2 + 1, 2):
            ans += piles[i]
        return ans