#include <limits.h>
#include <vector>

class Solution {
public:
    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
        std::vector<bool> result;
        int maximumCandy = 0; 

        // Find the largest candy
        for (int candy : candies)
        {
            maximumCandy = std::max(maximumCandy, candy);
        }

        // Check candy + extraCandies > largest candy
        for (int i=0; i < candies.size(); i++)
        {
            result.push_back(candies[i] + extraCandies >= maximumCandy);
        }

        return result;
    }
};

int main()
{
    return 0;
}