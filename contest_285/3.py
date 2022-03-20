class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: list[int]) -> list[int]:
        

        dp = [[0,0]] * (len(aliceArrows) + 1)
        shots = [0] * (len(aliceArrows) + 1)


        alice_score = 0
        
        #score doesn't even matter just matters where she shot
        # for i in range(len(aliceArrows)):
        #     alice_score += aliceArrows[i] * i


        for i in range(1,len(aliceArrows)):

            dp[i] = max(dp[i]

            #compare alice shots taken this round and see if it's worth shooting by comparing points


        
        return shots


test = Solution()
test.maximumBobPoints(3,[0,0,1,0,0,0,0,0,0,0,0,2])