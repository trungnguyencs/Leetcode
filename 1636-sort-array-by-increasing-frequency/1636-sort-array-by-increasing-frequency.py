class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        arr = sorted([(freq, num) for num, freq in counter.items()], key=lambda x: (x[0], -x[1]))
        ans = []
        for freq, num in arr:
            ans.extend([num] * freq)
        return ans