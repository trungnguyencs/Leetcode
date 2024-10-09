class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        pairs = list(zip(monsters, coins))
        pairs.sort()
        sortedMonsters = [m for m, _ in pairs]
        coins = [c for _, c in pairs]
        for i in range(1, len(coins)):
            coins[i] += coins[i-1]
        ans = []
        for h in heroes:
            i = bisect_right(sortedMonsters, h)
            ans.append(0 if i == 0 else coins[i-1])
        return ans