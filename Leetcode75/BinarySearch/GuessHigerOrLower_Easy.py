class Solution:
    def guessNumber(self, n: int) -> int:
        
        low, high = 1, n

        while low <= high:
            medium = (low + high) // 2
            
            if guess(medium) < 0:
                high = medium - 1
            elif guess(medium) > 0:
                low = medium + 1
            else:
                return medium