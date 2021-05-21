class Solution:
    def solve(self, nums):
        for i in range(0,len(nums)):
            if i == nums[i]:
                return nums[i]
                break
        return -1