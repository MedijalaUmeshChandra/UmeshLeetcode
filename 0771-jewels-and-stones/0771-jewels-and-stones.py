class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
       
                dici = {}
                for i in stones:
                    if i not in dici:
                        dici[i] = 1
                    else:
                        dici[i] += 1
                ans = 0
                for j in jewels:
                        if j in dici:
                            ans = ans + dici[j]
                return ans 