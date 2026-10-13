#include <stack>
#include <algorithm>

class MinStack {
private:
    // Each element in the stack stores: {current_value, minimum_value_so_far}
    std::stack<std::pair<int, int>> st;

public:
    MinStack() {
        // Constructor remains empty as the underlying std::stack initializes itself
    }
    
    void push(int val) {
        if (st.empty()) {
            st.push({val, val});
        } else {
            int current_min = st.top().second;
            st.push({val, std::min(val, current_min)});
        }
    }
    
    void pop() {
        if (!st.empty()) {
            st.pop();
        }
    }
    
    int top() {
        return st.top().first;
    }
    
    int getMin() {
        return st.top().second;
    }
};
