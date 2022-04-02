class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = []

        for i in range(len(s)-1,-1,-1):


