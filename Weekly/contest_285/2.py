#6028
class Solution:
    def countCollisions(self, directions: str) -> int:
        
        collisions = 0

        directions = [x for x in directions]

        for i in range(1,len(directions)):
            #car in front
            # if directions[i] == 'R' and directions[i+1] == 'S' or directions[i] == 'S' and directions[i+1] == 'L':
            #     collisions += 1
            # elif directions[i] == 'R' and directions[i+1] == 'L':
            #     collisions += 2

            #car behind
            if directions[i-1] == 'R' and directions[i] == 'S':
                collisions += 1
                directions[i] = 'S'
                lw = i-2
                while lw < i-1 and lw >-1:
                    if directions[lw] == 'R':
                        collisions +=1
                        lw -=1
                    else:
                        lw = i

            elif directions[i-1] == 'S' and directions[i] == 'L':
                collisions += 1
                directions[i] = 'S'

            elif directions[i-1] == 'R' and directions[i] == 'L':
                collisions += 2
                directions[i] = 'S'
                lw = i-2
                while lw < i-1 and lw >-1:
                    if directions[lw] == 'R':
                        collisions +=1
                        lw -=1
                    else:
                        lw = i


        return collisions

test = Solution()
print(test.countCollisions('RLRSLL'))
print(test.countCollisions('LLRR'))
print(test.countCollisions('SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR'))

#"SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR" Expected 20