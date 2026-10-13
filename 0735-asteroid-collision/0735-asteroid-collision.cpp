#include <vector>
#include <stack>
#include <cmath>

class Solution {
public:
    std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
        std::vector<int> st; // Acts as a stack for surviving asteroids

        for (int a : asteroids) {
            bool destroyed = false;
            // Collision happens only when stack top is moving right (>0) and current is moving left (<0)
            while (!st.empty() && st.back() > 0 && a < 0) {
                if (st.back() < -a) {
                    st.pop_back(); // Top asteroid explodes, keep checking
                    continue;
                } else if (st.back() == -a) {
                    st.pop_back(); // Both asteroids explode
                    destroyed = true;
                    break;
                } else {
                    destroyed = true; // Current asteroid explodes
                    break;
                }
            }
            if (!destroyed) {
                st.push_back(a);
            }
        }
        return st;
    }
};
