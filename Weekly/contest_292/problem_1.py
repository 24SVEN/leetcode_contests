class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        temp_count = 1
        final_list = []
        for i in range(len(num)-1):
            num1,num2 = int(num[i]),int(num[i+1])

            if num1 == num2:
                temp_count += 1
                if temp_count >= 3:
                    if num1 not in final_list:
                        final_list.append(num1)
            else:
                temp_count = 1



        return str(max(final_list)) * 3 if len(final_list) > 0 else ""



test = Solution()
print(test.largestGoodInteger("6777133339"))
print(test.largestGoodInteger("2300019"))
print(test.largestGoodInteger("42352338"))
        
