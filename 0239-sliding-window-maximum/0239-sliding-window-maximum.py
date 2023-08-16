class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for i, num in enumerate(nums):
            if q and i - q[0] >= k:
                q.popleft()
            while q and num > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans