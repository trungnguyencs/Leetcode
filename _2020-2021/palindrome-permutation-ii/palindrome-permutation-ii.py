class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        oddChars = list(filter(lambda i: counter[i] % 2 == 1, counter))
        if len(oddChars) > 1: return []      
        self.ans, arr = [], ['']*len(s)
        if len(oddChars) == 1:
            arr[len(s)//2] = oddChars[0]
            counter[oddChars[0]] -= 1
        self.backtrack(arr, counter, 0)
        return self.ans
    
    def backtrack(self, arr, counter, i):
        if i == len(arr)//2: self.ans.append(''.join(arr))
        for ch in counter:
            if counter[ch] == 0: continue
            arr[i] = arr[len(arr)-1-i] = ch
            counter[ch] -= 2
            self.backtrack(arr, counter, i+1)
            counter[ch] += 2