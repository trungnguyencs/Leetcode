class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        # if len(nums) % 2 == 0: i.e. [x0, x1, x2, x3]
        # => moves = (t - x0) + (t - x1) + (x2 - t) + (x3 - t) = (x3 - x0) + (x2 - x1) with some t: x1 < t <  x2
        # if len(nums) % 2 == 0: i.e. [x0, x1, x2, x3, x4]
        # => moves = (t - x0) + (t - x1) + (x4 - t) + (x3 - t) + abs(x2 - t) = (x4 - x0) + (x3 - x1) + abs(x2 - t)
        # => to make moves minimum: t equals to x2 (median) and moves = (x4 - x0) + (x3 - x1)
        moves = 0
        l, r = 0, len(nums) - 1
        while l < r:
            moves += nums[r] - nums[l]
            l += 1
            r -= 1
        return moves