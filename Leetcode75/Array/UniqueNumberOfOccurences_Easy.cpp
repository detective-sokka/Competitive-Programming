#include <set>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    bool uniqueOccurrences(std::vector<int>& arr) {
        std::set<int> occurenceHistory;
        std::unordered_map<int, int> occurenceCount;

        for (int element : arr)
        {
            occurenceCount[element] += 1;
        }

        for (std::pair<int, int> occurence : occurenceCount)
        {
            if (occurenceHistory.find(occurence.second) != occurenceHistory.end())
            {
                return false;
            }

            occurenceHistory.insert(occurence.second);
        }

        return true;
    }
};