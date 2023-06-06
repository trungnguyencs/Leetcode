class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all(arr[i+1] - arr[i] == arr[i+2] - arr[i+1] for i in range(len(arr) - 2))