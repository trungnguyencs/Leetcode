class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(str(len(s)) + ':' + s for s in strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []       
        l = 0
        while l < len(s):
            r = s.find(':', l)
            length = int(s[l:r])
            ans.append(s[r+1:r+1+length])
            l = r + 1 + length
        return ans
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))