# Note : This solutions is pretty slow. A faster solution uses bisect.bisect_left().

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []

        def return_pairs_after_binary_search(spell):            
            left = 0
            right = len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                strength = potions[mid] * spell
                if strength >= success and (mid == 0 or potions[mid-1] * spell < success):
                    return len(potions) - mid
                elif strength < success:
                    left = mid + 1
                else:
                    right = mid - 1

            return 0

        for spell in spells:
            result.append(return_pairs_after_binary_search(spell))

        return result