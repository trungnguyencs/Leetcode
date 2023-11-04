class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # ants do not differentiate so the result would be the same if ants don't change direction after meeting
        # so just find the longest time each ant has to reach the end
        ans = 0
        for pos in left:
            ans = max(ans, pos)
        for pos in right:
            ans = max(ans, n - pos)
        return ans