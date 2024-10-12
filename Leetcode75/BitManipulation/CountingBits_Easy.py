# Note: An observation is that number of 1s for a number is same as for number // 2. 
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        result = [0]

        for i in range(1, n+1):
            count = 0
            while i > 0:
                count = count + (i & 1)
                i = i >> 1
            result.append(count)
        
        return result