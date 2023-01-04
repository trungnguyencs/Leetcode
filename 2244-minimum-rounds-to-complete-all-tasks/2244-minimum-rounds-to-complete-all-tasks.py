class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        if 1 in counter.values(): return -1
        return sum(self.partition(v) for v in counter.values())
    
    def partition(self, num):
        if num % 3 == 0: return num//3
        return num//3 + 1