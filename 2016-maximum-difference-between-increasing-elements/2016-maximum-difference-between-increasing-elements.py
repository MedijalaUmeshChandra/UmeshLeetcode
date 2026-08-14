class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        ans = 0
        n=len(nums)
        minval = nums[0]
        for i in range(n):
            
            
                    ans = max(ans,nums[i]-minval)
                    minval = min(minval,nums[i])
                
             
        if(ans==0):
            return -1
        return ans
        