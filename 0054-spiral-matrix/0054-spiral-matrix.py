class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        R, C = len(matrix), len(matrix[0])
        l, r, t, b = 0, C - 1, 0, R - 1
        direction = 0
        while len(ans) < R * C:
            if direction == 0:
                for col in range(l, r + 1):
                    ans.append(matrix[t][col])
                t += 1
            elif direction == 1:
                for row in range(t, b + 1):
                    ans.append(matrix[row][r])
                r -= 1
            elif direction == 2:
                for col in range(r, l - 1, -1):
                    ans.append(matrix[b][col])
                b -= 1
            elif direction == 3:
                for row in range(b, t - 1, -1):
                    ans.append(matrix[row][l])
                l += 1
            direction = (direction + 1) % 4
        return ans