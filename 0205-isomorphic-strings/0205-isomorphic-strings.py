class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dici1 = {}
        dici = {}
        ans = True
        for i in range(len(s)):
            if s[i] not in dici:
                dici[s[i]] = t[i]
            else:
                if dici[s[i]] != t[i]:
                    return False
        for j in range(len(t)):
            if t[j] not in dici1:
                dici1[t[j]] = s[j]
            else:
                if dici1[t[j]] != s[j]:
                    return False
                    
        return True
        