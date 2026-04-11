class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = [i, -1]
            elif dic[num][1] == -1:
                dic[num] = [i, i - dic[num][0]]
            else:
                d = i - dic[num][0] + dic[num][1]
                dic[num] = [i, i - dic[num][0]]
                ans = min(ans, 2 * d)
        return ans if ans != float('inf') else -1