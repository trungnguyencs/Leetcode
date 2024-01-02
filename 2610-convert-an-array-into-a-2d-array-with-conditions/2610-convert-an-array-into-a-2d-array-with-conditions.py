class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        ans = [[] for _ in range(max(counter.values()))]
        for k, v in counter.items():
            for i in range(v):
                ans[i].append(k)
        return ans