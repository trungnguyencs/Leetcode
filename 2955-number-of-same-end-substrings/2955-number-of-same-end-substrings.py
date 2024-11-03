class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        counter = [0]*26
        dic = {-1: counter[:]}
        for i, ch in enumerate(s):
            counter[ord(ch) - ord('a')] += 1
            dic[i] = counter[:]
        return [self.sameEndSubstringCountHelper(s, dic[l - 1], dic[r]) for l, r in queries]
        
    def sameEndSubstringCountHelper(self, s, counterL, counterR):
        counterDiff = [b - a for a, b in zip(counterL, counterR)]
        return sum([n*(n + 1)//2 for n in counterDiff]) #if S has n character 'a' then it has n*(n+1)//2 substrings that both start and end with 'a'