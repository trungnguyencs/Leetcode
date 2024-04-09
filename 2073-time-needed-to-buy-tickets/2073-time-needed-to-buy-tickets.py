class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i, price in enumerate(tickets):
            if i <= k:
                time += min(price, tickets[k])
            else:
                time += min(price, tickets[k] - 1)
        return time