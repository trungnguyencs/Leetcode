class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqs = list(Counter(arr).values())
        freqs.sort()
        for i, freq in enumerate(freqs):
            if k < freq:
                return len(freqs) - i
            k -= freq
        return 0