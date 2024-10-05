# https://leetcode.com/discuss/interview-question/527769/lucid-oa-gridland

def gridCombinations(m, n, k):
    combos = []
    

    def getCombinations(string, m, n):
                
        if m == 0 or n == 0:        
            string  = string + 'V' * n + 'H' * m
            combos.append(string)
            return         

        getCombinations(string + 'H', m - 1 , n)                            
        getCombinations(string + 'V', m, n - 1)

    getCombinations("", m, n)

    return combos[k]

print(gridCombinations(3, 4, 4))
