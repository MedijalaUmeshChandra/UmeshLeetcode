class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dici = {}
        for val in nums:
            
            if val not in dici:
                dici[val] = 1
            else:
                dici[val] += 1
        for j in dici:
            n = dici[j]
            temp = n*(n-1)/2
            ans += temp
        return int(ans)

       




        