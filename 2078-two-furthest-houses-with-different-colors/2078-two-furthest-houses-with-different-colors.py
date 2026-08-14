class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
      
        ans = 0
        temp = 0
        n=len(colors)
        p = 0
        temp1 = 0
        q = n -1
        ans2 = 0
        for i in range(n-1,-1,-1):

                if(colors[i]!=colors[0]):
                    temp = abs(i-p)
                    ans = max(ans,temp)
                    break
        for j in range(n):
            if(colors[j]!=colors[n-1]):
                temp1 = abs(j-q)
                ans2 = max(ans2,temp1)
        ans = max(ans,ans2)
        return(ans)



