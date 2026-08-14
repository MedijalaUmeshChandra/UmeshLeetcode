class Solution:
    def defangIPaddr(self, li: str) -> str:
        ans = ""
        for i in range(len(li)):
            if li[i] != ".":
                ans = ans + li[i]
            if li[i] == ".":
                ans = ans + "[.]"
        return ans
             

    
   
   