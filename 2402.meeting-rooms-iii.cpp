/*
 * @lc app=leetcode id=2402 lang=cpp
 *
 * [2402] Meeting Rooms III
 */

// @lc code=start
#include <vector>
#include <queue>
#include <iostream>
class Solution
{
public:
    int mostBooked(int n, std::vector<std::vector<int>> &meetings)
    {
        std::vector<int> rooms(n);
        std::priority_queue<std::pair<long, int>, std::vector<std::pair<long, int>>, std::greater<std::pair<long, int>>> used; // min-heap for next available room (time, room)
        std::priority_queue<int, std::vector<int>, std::greater<int>> unused;                                                  // min-heap containing all available rooms
        // Initialize pq for unused rooms
        for (int i = 0; i < n; i++)
        {
            unused.push(i);
        }

        // Sort meetings by start time
        std::sort(meetings.begin(), meetings.end());

        for (auto &&meeting : meetings)
        {
            // Update list of available rooms
            while (used.top().first < meeting[0])
            {
                // Make the room available if the end time is earlier than the start time of current meeting
                unused.push(used.top().second);
                used.pop();
            }

            // There are empty rooms available - get smallest available room
            if (!unused.empty())
            {
                int room = unused.top();
                unused.pop();
                rooms[room]++;
                used.push(std::pair(meeting[1], room));
            }
            else
            {
                // No empty rooms available: take the next room available after a delay
                auto [end, room] = used.top();
                used.pop();
                rooms[room]++;
                long delay = end - meeting[0];
                used.push(std::pair(meeting[1] + delay, room));
            }
        }

        int ans = 0; // index of the room with the most meetings
        // std::cout << rooms[0] << std::endl;
        for (int i = 1; i < n; i++)
        {
            // std::cout << rooms[i] << std::endl;
            if (rooms[i] > rooms[ans])
                ans = i;
        }

        return ans;
    }
};
// @lc code=end
