class Solution:
    def find_smallest_bigger_number(self,num):
        if num<10:
            return 10

        num = num + 1
        li = list(str(num))

        i=0
        while (i+1) <= (len(li)-1):
            if li[i] == li[i+1]:
                idx = i+1

                #check if the digit is 9. If so add 1xxx
                if li[idx] == '9':
                    zeroes = len(li) - idx - 1
                    num = num + int('1' + zeroes * '0')
                    #replace all following digits with zero
                    li = list(str(num)[:idx+1]  + (len(str(num))-idx-1) * '0')
                    
                    #reset i to beginning
                    i=-1
                else:
                    li[idx] = str(int(li[idx]) + 1)
                    li = self.add_ones_and_zeroes(li,idx)
                    break
            i+=1
                    
        return int("".join(li))


    #this function converts all digits after an index to the 0 and 1 pattern
    def add_ones_and_zeroes(self,li,idx):
        swap = 1
        suffix = []
        for i in range(len(li)-1-idx):
            if swap == 1:
                suffix.append('0')
            else:
                suffix.append('1')
            swap *= -1

        return li[:idx+1] + suffix



#test cases
test = Solution()
print(test.find_smallest_bigger_number(66))
print(test.find_smallest_bigger_number(1000000))
print(test.find_smallest_bigger_number(100))
print(test.find_smallest_bigger_number(1))
print(test.find_smallest_bigger_number(910))
print(test.find_smallest_bigger_number(10099))
print(test.find_smallest_bigger_number(89898989899))
print(test.find_smallest_bigger_number(9989898989999898989899))

