class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        missing = -1
        n = len(nums)
        s = set()
        ans = []
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                duplicate = nums[i]
        for j in range(1,len(nums)+1):
            if j not in s:
                missing = j
        ans.append(duplicate)
        ans.append(missing)
        return ans
        
        