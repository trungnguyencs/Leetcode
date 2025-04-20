class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0
        for key, freq in counter.items():
            groupSize = key + 1
            groupCount = freq//groupSize if freq % groupSize == 0 else freq//groupSize + 1
            ans += groupSize * groupCount
        return ans