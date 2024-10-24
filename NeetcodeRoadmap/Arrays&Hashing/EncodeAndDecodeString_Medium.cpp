#include <string>
#include <vector>

class Solution {
public:

    std::string encode(std::vector<std::string>& strs) {
        std::string result = "";

        for (std::string word : strs)
        {
            result = result + std::to_string(word.length()) + '#';
            result += word;
        }

        return result;
    }

    std::vector<std::string> decode(std::string s) {
        
        std::vector<std::string> result;
        
        int i = 0;
        std::string wordLengthCounter = "";
        int wordLength = 0;

        while (i < s.length())
        {
            wordLengthCounter = "";
            wordLength = 0;

            while (s[i] != '#')
            {
                wordLengthCounter += s[i];
                i++;
            }

            i++;
            
            wordLength = std::stoi(wordLengthCounter);            
            result.push_back(s.substr(i, wordLength));
            i += wordLength;
        }

        return result;
    }
};
