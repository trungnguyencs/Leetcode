class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'G': x, y = x + dx, y + dy
            elif i == 'L': dx, dy = -dy, dx
            elif i == 'R': dx, dy = dy, -dx
        # 2 cases for a loop:
        # - robot returns to origin
        # - direction different than (0, 1) (=> will get back to origin after 1 or 3 more sequences)
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)