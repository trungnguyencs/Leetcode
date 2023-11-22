class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # iterate C*R will time out, so use BFS instead:
        ans = []
        q = deque([(0, 0)])
        visited = {(0, 0)}
        while q:
            r, c = q.popleft()
            ans.append(nums[r][c])
            if r + 1 < len(nums) and c < len(nums[r+1]) and (r + 1, c) not in visited:
                q.append((r + 1, c))
                visited.add((r + 1, c))
            if c + 1 < len(nums[r]) and (r, c + 1) not in visited:
                q.append((r, c + 1))
                visited.add((r, c + 1))
        return ans