#include <limits>
#include <vector>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int currentVolume = 0;
        int maxVolume = 0;

        while (left <= right)
        {
            currentVolume = (right - left) * std::min(height[left], height[right]);
            maxVolume = std::max(maxVolume, currentVolume);

            height[left] < height[right] ? left++ : right--;
        }

        return maxVolume;
    }
};