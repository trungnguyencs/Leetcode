class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        l, r, t, b = 0, C - 1, 0, R - 1
        direction = 0
        ans = []
        while len(ans) < R * C:
            if direction == 0:
                for i in range(l, r + 1):
                    ans.append(matrix[t][i])
                t += 1
            elif direction == 1:
                for i in range(t, b + 1):
                    ans.append(matrix[i][r])
                r -= 1
            elif direction == 2:
                for i in range(r, l - 1, -1):
                    ans.append(matrix[b][i])
                b -= 1
            else:
                for i in range(b, t - 1, -1):
                    ans.append(matrix[i][l])
                l += 1
            direction = (direction + 1) % 4
        return ans