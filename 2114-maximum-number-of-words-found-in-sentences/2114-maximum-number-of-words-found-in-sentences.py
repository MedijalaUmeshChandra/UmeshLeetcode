class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
       
        ans = 0
        for j in range(len(sentences)):
            one=sentences[j]
            temp = 1
            for i in range(len(one)):
                if one[i]==" ":
                    temp = temp + 1
                    
            ans = max(ans, temp)
        return ans
        