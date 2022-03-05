class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # similar to 198. House Robber
        ans = 0
        counter = Counter(nums)
        houseRobber = sorted(counter.keys())
        prev, cur = 0, houseRobber[0] * counter[houseRobber[0]]
        for i in range(1, len(houseRobber)):
            points = houseRobber[i] * counter[houseRobber[i]]
            if houseRobber[i] == houseRobber[i-1] + 1:
                prev, cur = cur, max(cur, prev + points)
            else:
                prev, cur = cur, cur + points
        return cur