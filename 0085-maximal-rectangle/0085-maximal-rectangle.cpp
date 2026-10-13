#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
private:
    int largestRectangleArea(const vector<int>& heights) {
        stack<int> st;
        int maxArea = 0;
        int n = heights.size();
        for (int i = 0; i <= n; ++i) {
            while (!st.empty() && (i == n || heights[st.top()] > heights[i])) {
                int h = heights[st.top()];
                st.pop();
                int width = st.empty() ? i : (i - st.top() - 1);
                maxArea = max(maxArea, h * width);
            }
            st.push(i);
        }
        return maxArea;
    }

public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        
        int rows = matrix.size();
        int cols = matrix[0].size();
        vector<int> heights(cols, 0);
        int maxRect = 0;

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                // Update histogram height: add 1 if '1', reset to 0 if '0'
                if (matrix[i][j] == '1') {
                    heights[j] += 1;
                } else {
                    heights[j] = 0;
                }
            }
            // Find largest rectangle in histogram for the current row
            maxRect = max(maxRect, largestRectangleArea(heights));
        }

        return maxRect;
    }
};
