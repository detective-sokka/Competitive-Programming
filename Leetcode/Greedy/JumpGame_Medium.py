# https://leetcode.com/problems/jump-game/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days
# Solution from Neetcode.io
class Solution:
    def canJump(self, nums: List[int]) -> bool:        
        # if len(nums) is 1 return True
        # if nums[0] is atleast len(nums) - 1 return True
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False