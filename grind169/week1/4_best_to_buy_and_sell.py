from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10000
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))

"""
// Kotlin version, just for runtime comparison
import kotlin.math.max
import kotlin.math.min

class Solution {
    fun maxProfit(prices: IntArray): Int {
        var min = Int.MAX_VALUE
        return prices.fold(0) { maxProfit, price ->
            min = min(min, price)
            val profit = price - min
            max(maxProfit, profit)
        }
    }
}

fun main() {
    println(Solution().maxProfit(intArrayOf(7,1,5,3,6,4)))
}
"""
