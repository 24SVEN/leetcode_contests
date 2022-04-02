class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: list[int]) -> list[int]:
        
        #points | shots taken
        dp = [list()] * (len(aliceArrows) + 1)
        shots = [0] * (len(aliceArrows) + 1)


        #need another list that stores max score possible with x given arrows


        alice_score = 0
        
        #score doesn't even matter just matters where she shot
        # for i in range(len(aliceArrows)):
        #     alice_score += aliceArrows[i] * i

        alice_shots = aliceArrows[0]

        #setting score at 11th round
        #if alice shot all of her arrows on 11th round, then automatic 0 points and 0 shots taken by Bob since it is an unwinnable round
        if aliceArrows[-1] == numArrows:
            dp[len(aliceArrows)-1] = [0,0]
        else:
            dp[len(aliceArrows)-1] = [11,aliceArrows[-1] + 1]

        #going bottom up dp
        for i in range(len(aliceArrows)-2,0):
            total_alice_shots += aliceArrows[i]
            

            #need to determine if it is worth it to shoot this round
            
            #shots Alice took
            current_alice_shots = aliceArrows[i]

            #shots needed to win the round
            shots_for_round = current_alice_shots + 1

            #score for winning
            points_for_round = shots_for_round * i
            
            #shots remaining
            shots_remaining = numArrows - shots_for_round
            dp[i] = max(dp[i+1],points_for_round)

            #compare alice shots taken this round and see if it's worth shooting by comparing points


        
        return shots


test = Solution()
test.maximumBobPoints(3,[0,0,1,0,0,0,0,0,0,0,0,2])