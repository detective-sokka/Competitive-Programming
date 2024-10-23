#include <vector>

class Solution {
public:
    int pivotIndex(std::vector<int>& nums) {
        
        int pivot = 0;
        int leftSum = 0, rightSum = 0;

        for (int i=0; i < nums.size(); i++)
        {
            rightSum += nums[i];
        }

        while (0 <= pivot && pivot < nums.size())
        {
            rightSum -= nums[pivot];

            if(leftSum == rightSum)
                return pivot;

            leftSum += nums[pivot++];
        }

        return -1;
    }
};

int main()
{
    return 0;
}