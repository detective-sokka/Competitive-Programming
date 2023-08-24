# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:        
        a_10 = 0
        b_10 = 0
        a_len = len(a)
        b_len = len(b)
        result_10 = 0

        i = 0 
        # convert a to decimal
        while i < a_len:
            if a[i] == '1':
                a_10 += 2 ** (a_len - i - 1)
            
            i += 1
        
        i = 0

        # convert b to decimal 
        while i < b_len:
            if b[i] == '1':
                b_10 += 2 ** (b_len - i - 1)
            
            i += 1
        
        # add them and return the sum in binary
        result_10 = a_10 + b_10
        result_str = ""
        
        # convert decimal to binary
        while result_10 > 0:
            result_str = ('0' if (result_10 % 2 == 0) else '1') + result_str            
            result_10 //= 2

        return result_str

print(Solution().addBinary("11", "1"))