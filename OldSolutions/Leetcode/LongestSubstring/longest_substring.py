class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        i, j,size = 0, 0, len(s)
        letters = set()
        result = 0


        while j < size:

            if s[j] in letters: 
                result = max(result, len(letters))
                letters.remove(s[i])
                i += 1 
                
            else:
                letters.add(s[j])
                j += 1
        
        result = max(result, len(letters))        
        return result
    
sol = Solution()


print(sol.lengthOfLongestSubstring(" "))

