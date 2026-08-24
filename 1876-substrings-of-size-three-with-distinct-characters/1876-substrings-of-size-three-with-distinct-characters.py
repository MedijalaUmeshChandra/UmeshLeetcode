class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        ans = []
        temp = ""
        l = 0
        fans=[]
        f=[]
        for r in range(n):
            temp = temp + s[r]
            if(r-l==3):
                temp = temp[1:]
                l = l + 1
            if(r-l+1==3):
                ans.append(temp)
        for item in ans:
            if (len(set(item)))==len(item):
                fans.append(item)
        return len(fans)
            


