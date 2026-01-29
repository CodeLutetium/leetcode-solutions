#include <array>
#include <climits>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <chrono>
#include "random.h"
class Solution
{
public:
    long long minimumCost(std::string source, std::string target, std::vector<char> &original,
                          std::vector<char> &changed, std::vector<int> &cost)
    {
        // Initialize result to store the total minimum cost
        long long totalCost = 0;

        // Initialize a 2D vector to store the minimum transformation cost
        // between any two characters
        std::vector<std::vector<long long>> minCost(26, std::vector<long long>(26, INT_MAX));

        // Fill the initial transformation costs from the given original,
        // changed, and cost arrays
        for (int i = 0; i < original.size(); ++i)
        {
            int startChar = original[i] - 'a';
            int endChar = changed[i] - 'a';
            minCost[startChar][endChar] =
                std::min(minCost[startChar][endChar], (long long)cost[i]);
        }

        // Use Floyd-Warshall algorithm to find the shortest path between any
        // two characters
        for (int k = 0; k < 26; ++k)
        {
            for (int i = 0; i < 26; ++i)
            {
                for (int j = 0; j < 26; ++j)
                {
                    minCost[i][j] =
                        std::min(minCost[i][j], minCost[i][k] + minCost[k][j]);
                }
            }
        }

        // Calculate the total minimum cost to transform the source string to
        // the target string
        for (int i = 0; i < source.size(); ++i)
        {
            if (source[i] == target[i])
            {
                continue;
            }
            int sourceChar = source[i] - 'a';
            int targetChar = target[i] - 'a';

            // If the transformation is not possible, return -1
            if (minCost[sourceChar][targetChar] >= INT_MAX)
            {
                return -1;
            }
            totalCost += minCost[sourceChar][targetChar];
        }

        return totalCost;
    }
};

void generateInputs()
{
    std::ofstream output("input.txt");
    const int src_len = 1e5;
    const int cost_len = 2e5;
    const int max_cost = 1e6;

    // source
    for (int i = 0; i < src_len; i++)
    {
        output << (char)('a' + Random::get(0, 25));
    }
    output << std::endl;

    // target
    for (int i = 0; i < src_len; i++)
    {
        output << (char)('a' + Random::get(0, 25));
    }
    output << std::endl;

    // original
    for (int i = 0; i < cost_len; i++)
    {
        output << (char)('a' + Random::get(0, 25));
    }
    output << std::endl;

    // changed
    for (int i = 0; i < cost_len; i++)
    {
        output << (char)('a' + Random::get(0, 25));
    }
    output << std::endl;

    // cost
    for (int i = 0; i < cost_len; i++)
    {
        output << Random::get(1, max_cost);
        if (i != cost_len - 1)
            output << ",";
    }
    output << std::endl;
    output.close();
}

int main()
{
    // generateInputs();

    std::ifstream input("input.txt");
    std::string source;
    std::string target;
    std::string buffer;
    std::vector<char> original;
    std::vector<char> changed;
    std::vector<int> cost;

    getline(input, source);
    getline(input, target);
    getline(input, buffer);
    original.reserve(buffer.size());
    for (char c : buffer)
    {
        original.push_back(c);
    }
    getline(input, buffer);
    changed.reserve(buffer.size());
    for (char c : buffer)
    {
        changed.push_back(c);
    }

    getline(input, buffer);
    std::stringstream ss(buffer);
    std::string token;
    while (getline(ss, token, ','))
    {
        cost.push_back(std::stoi(token));
    }

    input.close();

    using Clock = std::chrono::steady_clock;
    Solution solution;
    auto start = Clock::now();
    long long result = solution.minimumCost(source, target, original, changed, cost);
    auto end = Clock::now();
    auto diff = end - start;
    std::cout << "Result: " << result << std::endl;
    std::cout << "Time elapsed: "
              << std::chrono::duration<double, std::milli>(diff).count() << " ms" << std::endl;
    return 0;
}