/*
 * @lc app=leetcode id=18 lang=cpp
 *
 * [18] 4Sum
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution
{
public:
    std::vector<std::vector<int>> fourSum(std::vector<int> &nums, int target)
    {
        std::sort(nums.begin(), nums.end());
        int n = nums.size();
        std::vector<std::vector<int>> res;

        for (int i = 0; i < n - 3; i++)
        {
            // Skip duplicate numbers
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            // Next 4 numbers exceed target: break
            if ((long long)nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target)
                break;

            // Current number paired with largest 3 numbers smaller than target: continue
            if ((long long)nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target)
                continue;

            for (int j = i + 1; j < n - 2; j++)
            {
                // Skip duplicates
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;

                // Next 3 numbers exceed target: break
                if ((long long)nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target)
                    break;

                // Current numbers paired with largest 2 numbers smaller than target: continue
                if ((long long)nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target)
                    continue;

                int left = j + 1;
                int right = n - 1;

                while (left < right)
                {
                    long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target)
                    {
                        res.push_back({nums[i], nums[j], nums[left], nums[right]});

                        while (left < right && nums[left] == nums[left + 1])
                        {
                            left++;
                        }
                        while (left < right && nums[right] == nums[right - 1])
                        {
                            right--;
                        }
                        left++;
                        right--;
                    }
                    else if (sum < target)
                    {
                        left++;
                    }
                    else
                    {
                        right--;
                    }
                }
            }
        }

        return res;
    }
};
// @lc code=end
