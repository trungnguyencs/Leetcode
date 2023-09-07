class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        J, W = len(jobs), len(worker)
        ans = 0
        
        # #approach 1: O(JlogJ + WlogW), no need to update jobs
        # i = best = 0
        # for ability in worker:
        #     while i < J and ability >= jobs[i][0]:
        #         best = max(best, jobs[i][1])
        #         i += 1
        #     ans += best
        # return ans
    
        #approach 2: binary search O(jlogj + wlogj)
        #have to update jobs (in case of higher effort but lower profit)
        difficulty, profit = zip(*jobs)
        profit = list(profit)
        for i in range(1, J):
            profit[i] = max(profit[i], profit[i-1])
        for ability in worker:
            i = bisect_right(difficulty, ability)
            if i != 0: ans += profit[i-1]
        return ans