class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToColor = {}
        colorToBalls = defaultdict(int)
        ans = []
        colorCount = 0
        for ball, color in queries:
            if ball in ballToColor:
                oldColor = ballToColor[ball]
                colorToBalls[oldColor] -= 1
                if colorToBalls[oldColor] == 0:
                    colorCount -= 1
            ballToColor[ball] = color
            colorToBalls[color] += 1
            if colorToBalls[color] == 1:
                colorCount += 1
            ans.append(colorCount)
        return ans