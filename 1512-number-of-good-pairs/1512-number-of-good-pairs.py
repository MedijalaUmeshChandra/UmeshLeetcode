class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        n = len(nums)
        dici = {}
        for i in range(n):
            val = nums[i]
            if val not in dici:
                dici[val] = 1
            else:
                dici[val] += 1
        ans = 0
        for i in dici:
            n = dici[i]
            temp = n*(n-1)/2
            ans += temp
        return int(ans)




        