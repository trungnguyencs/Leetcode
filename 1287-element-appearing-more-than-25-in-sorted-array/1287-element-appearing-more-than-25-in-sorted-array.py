class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                freq += 1
                if freq > len(arr)//4:
                    return arr[i]
            else:
                freq, cur = 1, arr[i]
        return arr[0]