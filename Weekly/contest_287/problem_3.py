from curses import KEY_LEFT


class Solution:
    def maximumCandies(self, candies, k: int) -> int:
        
        total_candies = sum(candies)

        if total_candies < k:
            return 0


        smallest = min(total_candies)
        biggest = max(candies)


        dp = biggest * [0]

        