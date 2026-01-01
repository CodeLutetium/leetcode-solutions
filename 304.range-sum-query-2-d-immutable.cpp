/*
 * @lc app=leetcode id=304 lang=cpp
 *
 * [304] Range Sum Query 2D - Immutable
 */

// @lc code=start
#include <vector>

class NumMatrix
{
public:
    std::vector<std::vector<int>> psum;
    NumMatrix(std::vector<std::vector<int>> &matrix)
    {
        const size_t NUM_ROWS = matrix.size();
        const size_t NUM_COLS = NUM_ROWS > 0 ? matrix[0].size() : 0;
        // Calculate prefix sums. psum[i + 1][j + 1] = sum of all elements from 0,0 to i,j inclusive
        psum = std::vector<std::vector<int>>(NUM_ROWS + 1, std::vector<int>(NUM_COLS + 1, 0));

        for (size_t i = 1; i <= NUM_ROWS; i++)
        {
            for (size_t j = 1; j <= NUM_COLS; j++)
            {
                psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + matrix[i - 1][j - 1];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2)
    {
        return psum[row2 + 1][col2 + 1] - psum[row2 + 1][col1] - psum[row1][col2 + 1] + psum[row1][col1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
// @lc code=end
