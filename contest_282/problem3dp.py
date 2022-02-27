#attempt to include dp
import math

class Solution:
    def minimumTime(self, time, totalTrips: int) -> int:
        if len(time) == 1:
            return time[0]
        dp = 10000000 * [0]

        trip_count = 0

        return self.dfs(time,totalTrips,1,0,dp)

        
    def dfs(self,time,totalTrips,counter_time,current_trips,dp):


        current_trips = 0
        #for bus in time[0:counter_time]:
        #    current_trips += math.trunc(counter_time/bus)
        bustime = time[counter_time-1]
        dp[counter_time] = dp[counter_time-1] * counter_time + math.trunc(counter_time/bustime)
        current_trips = dp[counter_time]

        if totalTrips <= current_trips:
            return counter_time
        else:
            counter_time += 1
            return self.dfs(time,totalTrips, counter_time,current_trips,dp)


test = Solution()
# print(test.minimumTime([1,2,3],5))
#3
# print(test.minimumTime([2],1))
# #2

print(test.minimumTime([9,3,10,5],2))
