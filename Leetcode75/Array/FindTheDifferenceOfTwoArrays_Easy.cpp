#include <set>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> findDifference(std::vector<int>& nums1, std::vector<int>& nums2) {

        std::vector<std::vector<int>> result;
        result.push_back(std::vector<int>());
        result.push_back(std::vector<int>());

        std::set<int> set1;
        std::set<int> set2;

        for (int num : nums1)
        {
            set1.insert(num);
        }

        for (int num: nums2)
        {
            set2.insert(num);
        }

        for (int num : set1)
        {
            if (set2.find(num) == set2.end())            
            {
                result[0].push_back(num);
            }
        }

        for (int num : set2)
        {
            if (set1.find(num) == set1.end())            
            {
                result[1].push_back(num);
            }
        }

        return result;
    }
};

int main() 
{
    return 0;
}