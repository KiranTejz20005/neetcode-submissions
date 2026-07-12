class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        prefix = ""

        for i in range(len(first)):
            for s in strs:

                if i >=len(s) or s[i]!=first[i]:
                    return prefix

            prefix +=first[i]

        return prefix 
        