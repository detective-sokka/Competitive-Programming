#include <string>
#include <vector>

class Solution {
public:
    bool closeStrings(std::string word1, std::string word2) {
        
        if (word1.length() != word2.length())
            return false;

        std::vector<int> count1(26, 0);
        std::vector<int> count2(26, 0);

        for (char letter : word1)
        {
            count1[letter - 'a']++;
        }
        for (char letter : word2)
        {
            count2[letter - 'a']++;
        }

        // check if char present in word1 is not in word2 or vice versa
        for (int i=0; i < 26; i++)
        {
            if ((count1[i] == 0) ^ (count2[i] == 0))
                return false;
        }
        
        // check if counts are same. 
        std::sort(count1.begin(), count1.end());
        std::sort(count2.begin(), count2.end());        

        if (count1 == count2)
            return true;

        return false;
    }
};

int main()
{
    return 0;
}