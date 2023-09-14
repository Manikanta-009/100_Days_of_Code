# 100 Days of Code Challenge

## Day 12: Best Time to Buy and Sell Stock (Leetcode)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Check if the input list is empty, and return 0 if it is
        if not prices:
            return 0
        
        # Initialize the buy_price to the first price in the list
        buy_price = prices[0]
        
        # Initialize the max_profit to 0
        max_profit = 0
        
        # Iterate through the list of prices
        for new_price in prices:
            # If the current price is lower than the previously recorded buy_price,
            # update the buy_price to the current price.
            if new_price < buy_price:
                buy_price = new_price
            else:
                # If the current price is higher than the buy_price,
                # calculate the profit by subtracting the buy_price from the current price.
                # Update the max_profit if the calculated profit is higher than the current max_profit.
                max_profit = max(max_profit, new_price - buy_price)

        # Return the maximum profit that can be obtained
        return max_profit

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Example input: a list of stock prices
    prices = [7, 1, 5, 3, 6, 4]
    print("Prices: ", *prices)

    # Calculate the maximum profit using the maxProfit method of the Solution class
    max_profit = solution.maxProfit(prices)

    # Print the maximum profit
    print("Maximum Profit:", max_profit) # Maximum Profit: 5 (6-1)



"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""