class Solution:
    def largestInteger(self, num: int) -> int:
        
        num = [int(x) for x in str(num)]
        swap_count = 0

        i = 0
        evens = []
        odds = []

        for element in num:
            if element % 2 == 0:
                evens.append(element)
            else:
                odds.append(element)
        
        evens.sort(reverse= True)
        odds.sort(reverse = True)

        while i < len(num):
            if num[i] % 2 == 0 and evens:
                if num[i] == evens[0]:
                    evens.pop(0)

                elif num[i] < evens[0]:
                    idx = num[i+1:].index(evens[0])+i+1
                    temp = num[i]
                    num[i] = evens[0]
                    num[idx] = temp
                    evens.pop(0)
                    #swap_count += 1
            elif num[i] % 2 == 1 and odds:
                if num[i] == odds[0]:
                    odds.pop(0)

                elif num[i] < odds[0]:
                    idx = num[i+1:].index(odds[0])+i+1
                    temp = num[i]
                    num[i] = odds[0]
                    num[idx] = temp
                    odds.pop(0)
                    #swap_count += 1
            i+= 1
        num = [str(x) for x in num]
        return int("".join(num))

test = Solution()
print(test.largestInteger(1234)) #3412
print(test.largestInteger(65875)) #87655
print(test.largestInteger(60)) #60
print(test.largestInteger(251)) #251
print(test.largestInteger(266)) #662
print(test.largestInteger(3159)) #9513