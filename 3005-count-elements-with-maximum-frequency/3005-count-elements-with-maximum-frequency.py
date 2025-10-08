class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = maxFreq = 0
        counter = Counter()
        for num in nums:
            counter[num] += 1
            if counter[num] == maxFreq:
                ans += 1
            elif counter[num] > maxFreq:
                maxFreq = max(maxFreq, counter[num])
                ans = 1
        return ans * maxFreq