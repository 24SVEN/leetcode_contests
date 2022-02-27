#https://leetcode.com/problems/minimum-time-to-complete-trips/

import math


class Solution:
    def minimumTime(self, time, totalTrips: int) -> int:
        dp = totalTrips * [0]

        trip_count = 0

        return self.dfs(time,totalTrips,1,0)

        
    def dfs(self,time,totalTrips,counter_time,current_trips):


        current_trips = 0
        for bus in time[0:counter_time]:
            current_trips += math.trunc(counter_time/bus)
        
        
        if totalTrips <= current_trips:
            return counter_time
        else:
            counter_time += 1
            return self.dfs(time,totalTrips, counter_time,current_trips)




test = Solution()
# print(test.minimumTime([1,2,3],5))
#3
# print(test.minimumTime([2],1))
# #2

print(test.minimumTime([9,3,10,5],2))

#getting timeout error