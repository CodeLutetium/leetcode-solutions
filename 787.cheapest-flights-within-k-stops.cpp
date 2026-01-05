/*
 * @lc app=leetcode id=787 lang=cpp
 *
 * [787] Cheapest Flights Within K Stops
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <queue>

class Solution
{
public:
    struct QueueItem
    {
        int stops;
        int price;
        int dest;
    };

    int findCheapestPrice(int n, std::vector<std::vector<int>> &flights, int src, int dst, int k)
    {
        std::vector<std::vector<std::pair<int, int>>> graph(n, std::vector<std::pair<int, int>>()); // represented as an adj list

        for (const auto &flight : flights)
        {
            int src = flight[0];
            int dest = flight[1];
            int price = flight[2];

            graph[src].push_back(std::pair(dest, price));
        }

        std::vector<int> prices(n, __INT_MAX__); // best price to reach i

        std::queue<QueueItem> q;
        q.push(QueueItem(0, 0, src));

        while (!q.empty())
        {
            auto [stops, price, src] = q.front();
            q.pop();

            if (stops <= k + 1 && src == dst)
            {
                prices[dst] = std::min(prices[dst], price + prices[src]);
                continue;
            }

            if (stops > k)
                continue;

            for (const auto [d, p] : graph[src])
            {
                if (price + p < prices[d])
                {
                    q.push(QueueItem(stops + 1, price + p, d));
                    prices[d] = price + p;
                }
            }
        }

        if (prices[dst] == __INT_MAX__)
            return -1;

        return prices[dst];
    }
};
// @lc code=end
