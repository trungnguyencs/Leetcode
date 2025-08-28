class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        dic = defaultdict(list)
        for r in range(R):
            for c in range(C):
                dic[r-c].append(grid[r][c])
        for diff, nums in dic.items():
            if diff >= 0:
                nums.sort()
            else:
                nums.sort(reverse=True)
        for r in range(R):
            for c in range(C):
                grid[r][c] = dic[r-c].pop()
        return grid