class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = Counter()
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                ans += 8 * counter[prod] #Each pair has 8 tuple arrangements
                counter[prod] += 1
        return ans