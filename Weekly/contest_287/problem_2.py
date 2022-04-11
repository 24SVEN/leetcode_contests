class Solution:
    def findWinners(self, matches):
        
        winners = {}
        losers = {}


        for match in matches:
            winner = match[0]
            loser = match[1]

            winners[winner] = winners.get(winner,0) + 1
            losers[loser] = losers.get(loser,0) + 1

        
        lost_once = [player for player,number_loss in losers.items() if number_loss == 1]
        undefeated = [player for player,number_wins in winners.items()]

        final_winners = []
        for i in range(len(undefeated)-1,-1,-1):
            if undefeated[i] not in losers:
                final_winners.append(undefeated[i])
        final_winners.sort()
        lost_once.sort()

        return [final_winners,lost_once]

test = Solution()
print(test.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(test.findWinners([[2,3],[1,3],[5,4],[6,4]]))
