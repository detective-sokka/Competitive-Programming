#include <string>

class Solution {
public:
    void trimSpacesFromIndex(std::string& s, int index)
    {
        // Remove leading spaces
        int i = index, count = 0;        
        while(i < s.length() && s[i]==' ')
        {
            i++;
            count++;
        }
        
        if (count > 0)
            s.erase(index, count);
    }

    void reverseStringFromToIndex(std::string& s, int from, int to)
    {
        char temp;

        while (from < to)
        {   
            temp = s[from];
            s[from] = s[to];
            s[to] = temp;

            from++;
            to--;
        }
    }

    std::string reverseWords(std::string s) 
    {
        // Trim leading spaces
        trimSpacesFromIndex(s, 0);

        // reverse entire string 
        reverseStringFromToIndex(s, 0, s.length()-1);

        // Trim leading spaces again
        trimSpacesFromIndex(s, 0);

        // iterate over string reversing each word using two pointers
        int left = 0;
        int right = 0;
        int nextSpace = 0;
        while(left < s.length() && right < s.length()+1)
        {                
            if(s[right] == ' ' || right == s.length())
            {                   
                trimSpacesFromIndex(s, right+1);
                reverseStringFromToIndex(s, left, right-1);            
                left = right+1;
            }

            right++;
        }
        
        return s;
    }
};

int main()
{
    return 0;
}