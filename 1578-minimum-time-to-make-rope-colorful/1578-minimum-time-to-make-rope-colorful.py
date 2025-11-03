class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        maxTime = streakTime = neededTime[0]
        prevColor = colors[0]
        for i in range(1, len(colors)):
            if colors[i] == prevColor:
                streakTime += neededTime[i]
                maxTime = max(maxTime, neededTime[i])
            else:
                ans += streakTime - maxTime
                maxTime = streakTime = neededTime[i]
                prevColor = colors[i]
        return ans + (streakTime - maxTime)