#include <set>
#include <string>

class Solution {
public:
    std::string reverseVowels(std::string s) {
        std::set<char> vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'};
        char temp;
        int left = 0;
        int right = s.length() - 1;

        while (left <= right){
            
            if(vowels.find(s[left]) == vowels.end())
                left++;
            
            else if(vowels.find(s[right]) == vowels.end())
                right--;

            else{
                temp = s[left];
                s[left] = s[right];
                s[right] = temp;
                left++;
                right--;
            }
        }

        return s;
    }
};

int main()
{
    return 0;
}