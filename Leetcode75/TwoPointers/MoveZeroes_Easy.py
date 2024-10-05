class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == 0:
                nums.pop(left)
                nums.append(0)
                right = right - 1
                continue

            left = left + 1