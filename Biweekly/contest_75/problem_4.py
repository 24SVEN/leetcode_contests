from collections import deque

from numpy import csingle
class Solution:
    def sumScores(self, s: str) -> int:
        dp = []

        for i in range(len(s)-1,-1,-1):
            
            current_word = s[i:]
            cs = 0
            if len(current_word) < 3:
                
                for i in range(len(current_word)):
                    if current_word[i] == s[i]:
                        cs += 1
                    else:
                        break
                dp.append(cs)
            else:
                if len(current_word) == len(s) and current_word == s:
                    dp.append(len(s))
                    
                else:
                    breaked = False
                    for j in range(2):
                        if current_word[j] == s[j]:
                            cs += 1
                        else:
                            breaked = True
                            break
                    if breaked:
                        dp.append(cs)
                    else:
                        k = 2

                        while k < len(s) and k<len(current_word) and s[k] == current_word[k]:
                            
                            k+=1
                        dp.append(cs + dp[-k])

                


        return sum(dp)

test = Solution()
print(test.sumScores('babab')) #9
#print(test.sumScores('azbazbzaz')) #14


#print(test.sumScores('csstnwtobjxchdxnnzex')) #21

#print(len('csstnwtobjxchdxnnzex'))