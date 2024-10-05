class Solution:
    
    def groupAnagrams(self, strs):

        dictOfDictionaries = {}
        for string in strs: 
            letterDict = ''.join(sorted(string))
            
            if letterDict in dictOfDictionaries:
                dictOfDictionaries[letterDict].append(string)
                continue
            
            dictOfDictionaries[letterDict] = [string]
        
        result = list(dictOfDictionaries.values())
        return result


    
solution = Solution()

print("result is ", solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))