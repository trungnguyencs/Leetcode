class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        count = ans = 0
        for num in nums:
            if num % modulo == k:
                count += 1
            ans += prefixSum[(count - k) % modulo]
            prefixSum[count % modulo] += 1
        return ans