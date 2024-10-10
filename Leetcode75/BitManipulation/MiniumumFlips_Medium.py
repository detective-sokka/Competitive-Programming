# Note: There is a better solution that involves XOR
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            a_bit, b_bit, c_bit = a & 1, b & 1, c & 1

            if c_bit == 1: 
                if a_bit | b_bit == 0: # a=0, b=0, c=1
                    count = count + 1
            else:
                if a_bit & b_bit == 1: # a=1, b=1, c=0
                    count = count + 2
                elif a_bit | b_bit == 1: # a, b = 0,1 or 1,0 ; c = 0
                    count = count + 1

            a = a >> 1
            b = b >> 1
            c = c >> 1

        return count

example1 = Solution()

print(example1.minFlips(8, 3, 5))