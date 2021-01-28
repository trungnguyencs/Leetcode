class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicS, dicT = {}, {}
        for i in range(len(s)):
            cS, cT = s[i], t[i]
            if cS not in dicS: dicS[cS] = cT
            elif dicS[cS] != cT: return False
            if cT not in dicT: dicT[cT] = cS
            elif dicT[cT] != cS: return False            
        return True