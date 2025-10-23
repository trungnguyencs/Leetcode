class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = [int(c) for c in s]
        while len(arr) > 2:
            newArr = []
            for i in range(len(arr) - 1):
                newArr.append((arr[i] + arr[i+1]) % 10)
            arr = newArr
        return arr[0] == arr[1]