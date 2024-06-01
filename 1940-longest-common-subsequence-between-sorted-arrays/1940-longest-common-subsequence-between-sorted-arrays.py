class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        counter = Counter()
        for arr in arrays:
            for num in arr:
                counter[num] += 1
        return [key for key, val in counter.items() if val == len(arrays)]