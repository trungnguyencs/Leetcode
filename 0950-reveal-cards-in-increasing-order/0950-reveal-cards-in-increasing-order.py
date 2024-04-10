class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # simulate the process
        n = len(deck)
        ans = [0]*n
        deck.sort()
        q = deque(range(n))
        for card in deck:
            ans[q.popleft()] = card
            if q:
                q.append(q.popleft())
        return ans