class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        K = set()
        q = deque(initialBoxes)
        ans = 0
        while q and any((status[b] == 1) or (b in K) for b in q):
            b = q.popleft()
            if status[b] == 1 or b in K:
                ans += candies[b]
                q.extend(containedBoxes[b])
                K.update(keys[b])
            else:
                q.append(b)
        return ans