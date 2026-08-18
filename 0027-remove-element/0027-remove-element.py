class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ans = []
        
        for i in nums:
            if i != val:
                ans.append(i)
        for j in range(len(ans)):
            nums[j] = ans[j]

        return len(ans)