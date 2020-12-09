class Solution:
    def numPairsDivisibleBy60(self, times: List[int]) -> int:
        count, dic = 0, defaultdict(int)
        for time in times:
            count += dic[(60 - time) % 60]
            dic[time % 60] += 1
        return count
