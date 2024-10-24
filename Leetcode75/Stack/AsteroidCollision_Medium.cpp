#include <iostream>
#include <stack>
#include <vector>

// Note : This is a highly inefficient solution

class Solution {
public:
    std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
        
        std::stack<int> stack;
        std::vector<int> result;

        int previousAsteroid;

        for (int asteroid : asteroids)
        {
            while (asteroid < 0 && !stack.empty())
            {
                previousAsteroid = stack.top();

                if (previousAsteroid > 0)
                {
                    if (previousAsteroid > abs(asteroid))
                    {
                        asteroid = 0;
                    }
                    else if (previousAsteroid < abs(asteroid))
                    {
                        stack.pop();
                    }
                    else
                    {
                        asteroid = 0;
                        stack.pop();
                    }
                }        
                else 
                {
                    break;
                }        
            }

            if (asteroid != 0)
            {
                stack.push(asteroid);
                std::cout << "push " << asteroid << std::endl;
            }
        }
        
        while (!stack.empty())
        {
            result.insert(result.begin(), stack.top());
            stack.pop();
        }
        
        return result;
    }
};