class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        counter = Counter(A)
        uniq = [num for num in counter if counter[num] == 1]
        return max(uniq) if uniq else -1