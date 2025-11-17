class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        streak = float('inf')
        for i, num in enumerate(nums):
            if num == 0:
                streak += 1
            elif num == 1:
                if streak < k: return False
                streak = 0
        return True