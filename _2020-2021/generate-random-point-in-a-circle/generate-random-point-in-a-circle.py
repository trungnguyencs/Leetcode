class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.xCenter, self.yCenter, self.r = x_center, y_center, radius

    def randPoint(self) -> List[float]:
        x = random.uniform(self.xCenter - self.r, self.xCenter + self.r)
        y = random.uniform(self.yCenter - self.r, self.yCenter + self.r)
        if (x - self.xCenter)**2 + (y - self.yCenter)**2 <= self.r**2:
            return [x, y]
        return self.randPoint()


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()