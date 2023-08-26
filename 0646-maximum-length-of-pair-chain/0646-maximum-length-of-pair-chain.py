class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # dp solution O(n**2)
        # pairs.sort()
        # dp = [1]*len(pairs)
        # for i in range(1, len(pairs)):
        #     for j in range(i):
        #         if pairs[j][0] != pairs[i][0] and pairs[j][1] < pairs[i][0]:
        #             dp[i] = max(dp[i], 1 + dp[j])
        # return max(dp)
        
        # greedy solution O(nlogn)
        pairs.sort(key=lambda x: x[1])
        ans = 0
        lastEnd = float('-inf')
        for start, end in pairs:
            if start > lastEnd:
                ans += 1
                lastEnd = end
        return ans