class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        difference = goal - start
        
        return start ^ goal


test = Solution()
print(test.minBitFlips(10,7))