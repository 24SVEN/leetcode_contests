from locale import currency

from collections import defaultdict
class Solution:
    def appealSum(self, s: str) -> int:
        
        result = []
        #current_path = defaultdict(int)
        current_path = []
        self.dfs(0,result,current_path,s)
        return result
        #return sum(result)
    
    #current path is hashmap
    def dfs(self,idx,result,current_path,all_path):
        if idx > len(all_path):
            return 
        
        #result.append(1 if len(current_path) == 1 else len([key for key,val in current_path.items() if val == 1]))
        result.append(list(current_path))

        for i in range(idx,len(all_path)):
            #current_path[all_path[i]] += 1
            current_path.append(all_path[i])

            self.dfs(i+1,result,current_path,all_path)
            #backtrack
            #current_path[all_path[i]] -= 1
            current_path.pop()

        return result

test = Solution()
# print(test.appealSum("abbca"))
print(test.appealSum("code"))