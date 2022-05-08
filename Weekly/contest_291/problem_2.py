from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards) -> int:
        

        rw = 0
        result = float('inf')

        #value,[list of index]
        temp = defaultdict(list)
        while rw < len(cards):
            if cards[rw] in temp:
                num_min = max(temp[cards[rw]])
                result = min(result,rw-num_min+1)
            temp[cards[rw]].append(rw)
            rw += 1

        
        return result if result != float('inf') else -1

            # if cards[rw] == 770:
            #     pass
            # if cards[rw] in temp:
            #     #get index of temp
                
            #     if temp.count(cards[rw]) > 1:
            #         temp.reverse()
            #         idx = temp.index(cards[rw])
            #     else:
            #         idx = temp.index(cards[rw])

            #     #may need to get last index from reverse
            #     #check if there are more than 1
                

            #     if temp[idx] == cards[rw]:

            #         temp.append(cards[rw])
            #         #recreate temp
            #         temp = temp[idx:rw+1]

            #         result = min(result,len(temp))
                


            #     rw+=1
            # else:
            #     temp.append(cards[rw])
            #     rw += 1
            

test = Solution()
print(test.minimumCardPickup([3,4,2,3,4,7]))
print(test.minimumCardPickup([1,0,5,3]))
print(test.minimumCardPickup([70,37,70,41,1,62,71,49,38,50,29,76,29,41,22,66,88,18,85,53])) #expected 3
print(test.minimumCardPickup([95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6])) #expected 3

#[ (992, 2), (133, 2), (152, 2), (950, 2), (102, 2), (119, 2), (770, 2), (832, 2), (391, 3)]

print(test.minimumCardPickup([746,464,175,787,105,164,370,110,642,413,353,410,200,141,915,170,928,326,123,528,8,11,474,168,992,43,901,133,579,152,135,893,950,102,863,119,835,795,783,728,35,916,770,698,832,324,391,338,102,770,183,739,804,468,591,174,929,992,406,349,472,260,586,938,677,331,629,769,148,566,501,628,845,197,48,369,754,542,608,632,639,815,758,206,400,105,298,993,187,133,950,430,92,225,609,507,753,873,732,353,894,63,867,814,736,109,440,288,846,152,164,42,96,134,170,649,832,385,265,178,447,678,415,32,428,524,118,775,593,221,247,887,119,159,391,661,220,175,693,184,534,281,569,306,383,330,355,408,30,200,391,136,721,925]))
