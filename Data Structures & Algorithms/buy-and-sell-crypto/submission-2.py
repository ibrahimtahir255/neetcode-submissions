class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        U:
        Can we know the future price or do we have to go from left to right

        Edges cases:
        if prices = [] return 0
        if len(prices) == 1 return 0

        M:
        - sliding wondow with two pointers
        - move left pointer when there is a cheaper buy price
        """

        
        # Initilaize the two pinters buy and sell
        buy = 0
        sell = 1

        # initalize max profit
        max_profit = 0

        # loop while buy <= sell and sell< length of prices
        while sell < len(prices):
            # if buy > sell
            if prices[buy] > prices[sell]:
                # move buy to where sell is
                buy = sell
            # else sell > buy
            else:
                # calcualte profit
                profit = prices[sell] - prices[buy]
                max_profit = max(profit,max_profit)
            # increment sell
            sell += 1

        return max_profit
        