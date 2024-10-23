#include <queue>

class RecentCounter {
    std::queue<int> times;
    int count;

public:
    RecentCounter() {
        count = 0;
    }
    
    int ping(int t) {
        
        times.push(t);
        count++;

        int result = 0;
        
        while (!(times.empty()) && times.front() < (t-3000))
        {
            times.pop();
            count--;
        }
        
        return count;
    }
};

int main()
{
    return 0;
}