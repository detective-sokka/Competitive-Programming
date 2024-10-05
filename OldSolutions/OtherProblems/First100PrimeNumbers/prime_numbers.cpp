#include <iostream>

int main (int argn, const char * args[]) {    

    for(auto candidate = 2; candidate < 101; candidate += 2) {

        for (auto factor = 2; factor < std::sqrt(candidate); factor++) {

            if (candidate % factor == 0) {
                std::cout << std::format("{} ", candidate);
            }
        }
    }

}