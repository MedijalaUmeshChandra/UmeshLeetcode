class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
       
                   ans = 0
                   for i in range(len(jewels)):
                      for j in range(len(stones)):
                          chi=jewels[i]
                          chj=stones[j]
                          if chi==chj:
                              ans += 1
                   return(ans)