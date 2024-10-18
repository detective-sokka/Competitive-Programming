#include <string>
#include <iostream>

class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {

        int i = 0;
        std::string result;
        int i1 = 0, i2 = 0;
        
        for (i = 0; i < word1.length() + word2.length(); i++)
        {
            if((i1 < word1.length() && i%2 == 0) || i2 >= word2.length())
            {
                result = result + word1[i1++];
            }
            else
            {
                result = result + word2[i2++];
            }
        }

        return result;
    }
};

int main()
{
    Solution *solution = new Solution();
    std::cout << solution->mergeAlternately("ABCABC", "ABC");
    delete solution;
    return 0;
}