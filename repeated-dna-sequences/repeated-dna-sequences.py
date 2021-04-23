class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        seen, ans = set(), set()
        hashcode = 0
        for i, ch in enumerate(s):
            hashcode = hashcode*4 + dic[ch]
            if i == 9: seen.add(hashcode)
            if i < 10: continue
            hashcode -= dic[s[i-10]]*(4**10)
            if hashcode in seen: ans.add(s[i-9:i+1])
            else: seen.add(hashcode)
        return ans           