class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        times = [1,5,15,60]

        #convert time
        hours = int(current[0:2]) * 60
        minutes = int(current[3:])
        total_current = hours + minutes

        hours = int(correct[0:2]) * 60
        minutes = int(correct[3:])
        total_correct = hours + minutes

        total = abs(total_current - total_correct)

        count = 0
        while total != 0:
            time = times.pop()

            if total // time > 0:
                total -= time
                count += 1
                times.append(time)

            

        return count            

        #just try from largest to smallest




test = Solution()
print(test.convertTime('02:30','04:35'))
print(test.convertTime('11:00','11:01'))