class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        while len(sticks) != 1:
            newStick = heappop(sticks) + heappop(sticks)
            cost += newStick
            heappush(sticks, newStick)
        return cost