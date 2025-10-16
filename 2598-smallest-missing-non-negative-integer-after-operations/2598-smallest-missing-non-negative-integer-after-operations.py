class Solution:
    def findSmallestInteger(self, nums: List[int], k: int) -> int:
        counter = {r: 0 for r in range(k)}
        for num in nums:
            counter[num % k] += 1
        arr = [(freq, r) for r, freq in counter.items()]
        freq, r = min(arr)
        return freq * k + r