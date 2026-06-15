class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = [(d, p) for d, p in zip(difficulty, profit)]
        arr.sort() #sort based on job difficulty
        difficulty = [d for d, _ in arr]
        profit = [p for _, p in arr]
        for i in range(1, len(difficulty)):
            #now profit i in the maxProfit we can get from any job that has difficulty <= difficulty[i]
            profit[i] = max(profit[i-1], profit[i])
        ans = 0
        for w in worker:
            i = bisect_right(difficulty, w)
            if i == 0: continue #this worker can't do any job
            ans += profit[i-1]
        return ans