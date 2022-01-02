class Solution:
    def numPairsDivisibleBy60(self, times: List[int]) -> int:
        dic = Counter()
        for t in times:
            dic[t % 60] += 1
        print(dic)
        ans = 0
        for k, v in dic.items():
            if k == 30 or k == 0:
                ans += v*(v-1)
            else:
                ans += v*dic[60 - k]
        return ans//2