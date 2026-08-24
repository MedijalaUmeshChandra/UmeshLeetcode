class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        ans = []
        fans = []
        for i in range(n):
            for j in range(i,n):
                temp = ""
                for k in range(i,j+1):
                    temp = temp + s[k]
                if len(temp)==3:
                    ans.append(temp)
        for item in ans:
            if (len(set(item)))==len(item):
                fans.append(item)
        return len(fans)

