# Leetcode: 121. Best Time to Buy and Sell Stock
# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        
        # for each price in prices, we must:
        # 1. update min_price if price is less than min_price (always buy at the lowest price)
        
        for price in prices:
            if price < min_price:
                
                # greedy approach: always buy at the lowest price
                min_price = min(min_price, price)

            # else, we must update the max_profit if the selling price is higher than the buying price
            elif price - min_price > max_profit:
                profit = price - min_price
                
                # greedy approach: always sell at the highest price
                max_profit = max(max_profit, profit)
        return max_profit
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))  # 5
    print(s.maxProfit([7,6,4,3,1]))  # 0
    print(s.maxProfit([1,2]))  # 1
    print(s.maxProfit([2,4,1]))  # 2
