class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #the target number should be the median if length is odd
        #or any of the 2 middle numbers if length is even
        #Proof with example x1 - x2 - x3:
        #If we insert target t to the left or the right of x2, it will increase the sum(xi - t) by abs(x2 - t)
        #so to minimize sum(xi - t), t must be x2
        mod = grid[0][0] % x
        nums = [grid[r][c] for r in range(len(grid)) for c in range(len(grid[0]))]
        if any(num % x != mod for num in nums): return -1
        nums.sort()
        middle = nums[len(nums)//2]
        return sum(abs(num - middle)//x for num in nums)