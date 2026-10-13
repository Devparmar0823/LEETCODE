#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        int n = arr.size();
        int mod = 1e9 + 7;
        
        vector<int> left(n), right(n);
        stack<int> st;
        
        // Previous lesser element (strict or non-strict to avoid duplicates)
        for (int i = 0; i < n; i++) {
            while (!st.empty() && arr[st.top()] >= arr[i]) {
                st.pop();
            }
            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }
        
        while (!st.empty()) st.pop();
        
        // Next lesser element (strict to handle duplicate values cleanly)
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && arr[st.top()] > arr[i]) {
                st.pop();
            }
            right[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        
        long long totalSum = 0;
        for (int i = 0; i < n; i++) {
            long long leftSpan = i - left[i];
            long long rightSpan = right[i] - i;
            long long contribution = (arr[i] * leftSpan % mod) * rightSpan % mod;
            totalSum = (totalSum + contribution) % mod;
        }
        
        return totalSum;
    }
};
