// Note : There is a waay more space efficient solution.
// Note : No way this is an easy problem. I would rate it Medium - Hard

#include <string>

class Solution {
public:
    bool multiplyDivisorAndCompare(std::string divident, std::string divisor)
    {
        if (divident.length() % divisor.length() != 0)
            return false;

        std::string constructedFromDivisor = "";

        for (int i = 0; i < divident.length(); i += divisor.length())
        {
            constructedFromDivisor += divisor;
        }

        return divident == constructedFromDivisor;
    }

    std::string gcdOfStrings(std::string str1, std::string str2) {
        
        // check if minimum string itself is the greatest common divisor.
        std::string divisor = str1.length() < str2.length() ? str1 : str2;
        std::string divident = str1.length() < str2.length() ? str2 : str1;

        // decrement divisor until gcd is reached
        for (int i = divisor.length(); i >= 1; i--)
        {
            if (divisor.length() % i == 0 && multiplyDivisorAndCompare(divisor, divisor.substr(0, i)))
            {
                if (multiplyDivisorAndCompare(divident, divisor.substr(0, i)))
                {                 
                    return divisor.substr(0, i);
                }
            }   
        }

        // if not reached return "" 
        return "";
    }
};

int main()
{
    return 0;
}