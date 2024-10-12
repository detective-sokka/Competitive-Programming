class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set()
        for number in nums:
            if number not in nums_set:
                nums_set.add(number)
            else:
                nums_set.remove(number)

        return nums_set.pop()