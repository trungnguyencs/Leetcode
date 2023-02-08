class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = {0}
        q = deque([(0, 0)])
        while q:
            for _ in range(len(q)):
                cur, d = q.popleft()
                if cur == len(nums) - 1: return d
                for i in range(1, nums[cur] + 1):
                    if cur + i not in visited and cur + i < len(nums):
                        visited.add(cur + i)
                        q.append((cur + i, d + 1))
        return -1