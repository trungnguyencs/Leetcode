class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #logic is similar to 370. Range Addition
        #add x to range [l, r] is equivalent to add x to range [l, n-1] plus add -x to range [r+1, n-1]
        arr = [0]*len(s)
        self.rangeAddition(arr, shifts)
        ans = []
        for ch, val in zip(s, arr):
            ans.append(self.shiftLetter(ch, val))
        return ''.join(ans)

    def rangeAddition(self, arr, shifts):
        for l, r, direction in shifts:
            val = 1 if direction == 1 else -1
            arr[l] += val
            if r != len(arr) - 1:
                arr[r+1] -= val
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]

    def shiftLetter(self, ch, val):
        offset = (ord(ch) - ord('a') + val) % 26
        return chr(ord('a') + offset)