#include <vector>

class Solution {
public:
    double findMaxAverage(std::vector<int>& nums, int k) {
        double maximumAverage = 0.0;
        double windowTotal = 0.0;
        int left = 0;
        int right = k - 1;

        // Calculate average of window
        for (int i = left; i <= right; i++)
        {
            windowTotal += nums[i];
        }

        maximumAverage = windowTotal/k;

        // Slide window to the right by 1
        for (int i = right + 1; i < nums.size(); i++)
        {
            windowTotal = windowTotal + nums[i] - nums[left++];                        
            maximumAverage = maximumAverage < windowTotal/k ? windowTotal/k: maximumAverage;            
        }
        // return maximum average 
        return maximumAverage;
    }
};

int main()
{
    return 0;
}