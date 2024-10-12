class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        
        if len(s) == 0:
            return True

        if len(s) > len(t):
            return False

        for char in t:            
            if char == s[s_ptr]:
                s_ptr = s_ptr + 1
            
            if s_ptr == len(s):
                return True
        
        
        return False
