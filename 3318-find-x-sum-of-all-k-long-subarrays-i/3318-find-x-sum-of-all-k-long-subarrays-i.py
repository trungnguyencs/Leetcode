class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        counter = Counter()
        for i, num in enumerate(nums):
            counter[num] += 1
            if i >= k:
                counter[nums[i-k]] -= 1
            if i >= k - 1:
                arr = sorted([(freq, num) for num, freq in counter.items()], reverse=True)
                xSum = sum([num * freq for num, freq in arr[:x]])
                ans.append(xSum)
        return ans