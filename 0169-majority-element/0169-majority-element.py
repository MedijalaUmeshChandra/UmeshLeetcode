class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        
        ans = n/2
        dici = {}
        for i in range(n):
            val = nums[i]
            if val not in dici:
                dici[val] = 1
            else:
        
                dici[val] += 1


            if dici[val] > ans:
                return val

        