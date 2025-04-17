class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        ans = 0
        for i, num in enumerate(nums):
            lst = dic[num]
            for j in lst:
                if i * j % k == 0:
                    ans += 1
            lst.append(i)
        return ans