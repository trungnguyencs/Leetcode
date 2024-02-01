class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if i % 3 == 0:
                cur = []
            cur.append(num)
            if i % 3 == 2:
                if cur[2] - cur[0] > k: return []
                ans.append(cur)
        return ans