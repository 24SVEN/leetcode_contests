class Solution:
    def digitSum(self, s: str, k: int) -> str:

        
        summed = []

        list_s = list(s)

        while len(list_s) > k:
            num_groups = len(list_s) / k

            if num_groups != int(len(list_s) / k):
                num_groups = int(num_groups + 1)


            summed = []
            for i in range(int(num_groups)):
                temp = []
                for i in range(k):
                    if len(list_s) > 0:
                        num = list_s.pop(0)
                        temp.append(int(num))

                summed.append(str(sum(temp)))

            summed = "".join(summed)
            list_s = list(summed)
        
        return "".join(list_s)
        

test = Solution()
#print(test.digitSum('11111222223',3))
#print(test.digitSum('00000000',3))
print(test.digitSum('01234567890',2))
