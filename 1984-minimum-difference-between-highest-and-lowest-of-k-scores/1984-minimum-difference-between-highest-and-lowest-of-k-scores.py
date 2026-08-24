class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        l=0
        temp=[]
        ans=[]
        minval = float("inf")
        for r in range(n):
            temp.append(nums[r])
            if(r-l==k):
                temp.remove(nums[l])
                l += 1
            if(r-l+1==k):
                ans.append(temp.copy())
        for i in ans:
            diff = i[-1] - i[0]
            if diff<minval:
                minval = diff
        return minval


        