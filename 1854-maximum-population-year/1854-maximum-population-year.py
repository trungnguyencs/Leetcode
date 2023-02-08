class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        counter = Counter()
        for b, d in logs:
            for i in range(b, d):
                counter[i] += 1
        return max([y for y in counter], key=lambda y: (counter[y], -y))