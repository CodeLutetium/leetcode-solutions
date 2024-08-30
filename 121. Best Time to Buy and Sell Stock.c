int maxProfit(int* prices, int pricesSize) {
    // Edge case: only 1 item in prices
    if (pricesSize == 1)
        return 0;

    int max_profit = 0;
    int buy = 0;
    int sell = 1;

    while (sell < pricesSize) {
        if (prices[sell] > prices[buy]) {
            if (prices[sell] - prices[buy] > max_profit) {
                max_profit = prices[sell] - prices[buy];
            }
        } else {
            buy = sell;
        }
        sell++;
    }
    return max_profit;
}