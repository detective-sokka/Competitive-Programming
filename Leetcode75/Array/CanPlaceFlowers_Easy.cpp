#include <vector>

class Solution {
public:

    bool canPlaceFlowers(std::vector<int>& flowerbed, int n) {
        
        int count = 0;

        for (int i=0; i < flowerbed.size(); i++)
        {
            bool leftFlowerbedEmpty = (i == 0 || flowerbed[i-1] == 0);
            bool rightFlowerbedEmpty = (i == flowerbed.size() - 1 || flowerbed[i+1] == 0);

            if (flowerbed[i] == 0 && leftFlowerbedEmpty && rightFlowerbedEmpty)
            {
                flowerbed[i] = 1;
                count++;
            }
        }

        return count >= n;
    }
};

int main()
{
    return 0;
}