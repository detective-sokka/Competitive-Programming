#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int leftProduct = 1, rightProduct = 1;        
        std::vector<int> result(nums.size(), 1);

        // Compute left product
        for (int i = 0; i < nums.size(); i++)
        {   
            result[i] *= leftProduct;
            leftProduct *= nums[i];
        }

        // Compute right product
        for (int i = nums.size() - 1; i >= 0; i--)
        {
            result[i] *= rightProduct;
            rightProduct *= nums[i];
            std::cout << result[i] << ' ';
        }

        return result;
    }
};

int main()
{
    return 0;
}