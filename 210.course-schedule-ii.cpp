/*
 * @lc app=leetcode id=210 lang=cpp
 *
 * [210] Course Schedule II
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
#include <queue>

using namespace std;
class Solution
{
public:
    using QueueItem = pair<int, int>; // (indegree, course)

    vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites)
    {
        // Store the prerequisites as an adjacency list
        vector<vector<int>> adj(numCourses);
        // indegree[i] represents number of nodes connected to node i.
        vector<int> indegree(numCourses);
        for (auto &&prereq : prerequisites)
        {
            adj[prereq[1]].push_back(prereq[0]);
            indegree[prereq[0]]++;
        }

        // Add source node (indegree = 0) into the queue
        queue<int> queue;
        for (size_t i = 0; i < numCourses; i++)
        {
            if (indegree[i] == 0)
                queue.push(i);
        }

        vector<int> res;
        res.reserve(numCourses);

        while (!queue.empty())
        {
            int course = queue.front();
            queue.pop();

            res.push_back(course);

            // Add neighbours
            for (auto &&next : adj[course])
            {
                indegree[next]--;

                // Add to queue if its 0
                if (indegree[next] == 0)
                    queue.push(next);
            }
        }

        if (res.size() != numCourses)
            return {};

        return res;
    }
};
// @lc code=end
