class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # We can bring any number to index 0 by reversing the array from index 0 to the first occurence of the item
        # Repeat the process for index 1, 2, 3, etc
        return Counter(arr) == Counter(target)