class Solution:
    def minimumRounds(self, tasks) -> int:
        
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task,0) + 1
        
        count = 0
        for task,val in hashmap.items():
            if val == 1:
                return -1
            while val % 3 != 0:
                count += 1
                val -= 2
            count += (val / 3)
        return int(count)
        
        # tasks.sort()
        # return self.dfs(tasks,0)



        # i = 0
        # answer = 0
        # while i < len(tasks):
        #     count = 0

        #     while count+1 < len(tasks) and tasks[count+1] == tasks[count]:
        #         count += 1

        #     if tasks[-1] == 
            
        #     if count % 3 == 0:
        #         i += count
        #         answer += (count/3)
        #     elif count % 2 == 0:
        #         i += count
        #         answer += (count/2)
        #     else:
        #         return -1
        
        # return answer
        
    # def dfs(self,tasks,count_round):
    #     if len(tasks) == 0:
    #         return count_round
    #     if len(tasks) == 1:
    #         return -1

    #     two_tasks = tasks[:2]
    #     three_tasks = tasks[:3]

    #     #check if all are same digits
    #     if len(set(two_tasks)) > 1 and len(set(three_tasks)) > 1:
    #         return-1

    #     if len(two_tasks) ==2 and len(three_tasks) ==3 and len(set(two_tasks)) == 1 and len(set(three_tasks)) == 1:
    #         res1 = self.dfs(tasks[2:],count_round+1)
    #         res2 = self.dfs(tasks[3:],count_round + 1)
    #     elif len(set(two_tasks)) == 1 and len(set(three_tasks)) > 1:
    #         res1 = self.dfs(tasks[2:],count_round+1)
    #         res2 =-1
    #     elif len(set(two_tasks)) > 1 and len(set(three_tasks)) == 1:
    #         res1 = -1
    #         res2 = self.dfs(tasks[3:],count_round+1)
    #     else:
    #         res1 = self.dfs(tasks[2:],count_round+1)
    #         res2 = -1

    #     if res1 == -1 and res2 == -1:
    #         return -1
    #     elif res1 == -1:
    #         return res2
    #     elif res2==-1:
    #         return res1
    #     else:
    #         return min(res1,res2)





test = Solution()
#print(test.minimumRounds([2,2,3,3,2,4,4,4,4,4]))

#print(test.minimumRounds([2,2]))
#print(test.minimumRounds([9,9,9,11,11,22,22,22,22,55,55]))
print(test.minimumRounds([2,2,3,3,2,4,4,4,4,4]))
