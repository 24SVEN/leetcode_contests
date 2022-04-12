from cgitb import small


class Solution:
    def minimizeResult(self, expression: str) -> str:
        
        left,right = expression.split('+')
        smallest = [float('inf'),'']
        for i in range(len(left)):
            for j in range(len(right)):

                a=1
                if i>0:
                    a = left[:i]

                b = left[i:len(left)]
                c = right[:len(right)-j]
                
                d = 1
                if j> 0:
                    d = right[len(right)-j:]


                calculation = int(a) * ( int(b) + int(c)) *  int(d)

                if calculation < smallest[0]:
                    smallest[0] = calculation

                    if a == 1 and d == 1:
                        smallest[1] = '(' + b + '+' + c + ')'
                    elif a == 1:
                        smallest[1] = '(' + b + '+' + c + ')' + str(d)
                    elif d==1:
                        smallest[1] = str(a) + '(' + b + '+' + c + ')'
                    else:
                        smallest[1] = str(a) + '(' + b + '+' + c + ')' + str(d)


        return smallest[1]


test = Solution()
print(test.minimizeResult('247+38'))
print(test.minimizeResult('12+34'))

print(test.minimizeResult('999+999'))

print(test.minimizeResult('1+1'))

print(test.minimizeResult("6+253"))