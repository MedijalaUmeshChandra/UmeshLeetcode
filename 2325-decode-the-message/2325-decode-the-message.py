class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dici ={}
        temp = 97
        for i in key:
            if i!=" " and i not in dici:
                dici[i] = chr(temp)
                temp += 1
        ans = ""
        for j in message:
            if j==" ":
                ans = ans + " "
            elif j in dici:
                ans = ans + dici[j]
        return ans

        