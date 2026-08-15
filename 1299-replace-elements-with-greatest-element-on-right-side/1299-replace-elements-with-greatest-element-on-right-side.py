class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ans = []
        n = len(arr)
        maxval = -1
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = maxval
            maxval = max(maxval,temp)
        return arr
        

                   
                        
        
        return(ans + [-1])