// Note : Question requires O(1) space to be used
// Note : range-based loop is a c++ 11 feature
#include <unordered_map>
#include <vector>


class Solution {
public:
    int findDuplicate(std::vector<int>& nums) {
        int i, j;
        std::unordered_map <int, int> nums_map;
        
        for (int num: nums)
        {
            nums_map[num]++;

            if (nums_map[num] > 1)
            {
                return num;
            }
        }

        return -1;
    }
};

int main()
{
    return 0;
}