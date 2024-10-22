#include <vector>

class Solution {
public:
    int largestAltitude(std::vector<int>& gain) {
        int currentAltitude = 0;
        int maxAltitude = 0;

        for (int netAltitude : gain)
        {
            currentAltitude += netAltitude;
            maxAltitude = currentAltitude > maxAltitude ? currentAltitude : maxAltitude;
        }

        return maxAltitude;
    }
};

int main()
{
    return 0;
}