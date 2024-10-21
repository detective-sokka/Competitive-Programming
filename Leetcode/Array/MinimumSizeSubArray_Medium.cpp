#include <algorithm>
#include <limits.h>
#include <vector>

class Solution {
public:
    int minSubArrayLen(int target, std::vector<int>& nums) {
        int left = 0;
        int right = 0;
        int sum = nums[0];
        int minimumSubarraySize = INT_MAX;

        while (left <= right)
        {
            if (sum < target)
            {
                ++right;
                if(right == nums.size())
                {
                    break;
                }
                
                sum += nums[right];
            }
            else
            {
                minimumSubarraySize = std::min(minimumSubarraySize, right - left + 1);
                sum = sum - nums[left];
                left++;
            }
        }

        return minimumSubarraySize < INT_MAX ? minimumSubarraySize : 0;
    }
};

int main()
{
    return 0;
}