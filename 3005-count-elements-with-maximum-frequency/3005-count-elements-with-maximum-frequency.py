class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = maxFreq = 0
        counter = Counter()
        for num in nums:
            counter[num] += 1
            if counter[num] == maxFreq:
                ans += maxFreq
            elif counter[num] > maxFreq:
                maxFreq = counter[num]
                ans = maxFreq
        return ans