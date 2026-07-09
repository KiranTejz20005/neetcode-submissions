from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i<n:
            j=i
            while j<n and s[j] !=':':
                j+=1
            
            length = int(s[i:j])

            start = j+1

            res.append(s[start:start + length])

            i = start+length
        return res
