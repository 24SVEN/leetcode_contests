class Solution:
    def countLatticePoints(self, circles) -> int:

        result = set()
        for circle in circles:
            radius = circle[2]
            x = circle[0]
            y= circle[1]

            possible_points = []

            for i in range(x-radius,radius+x+1):
                for j in range(y-radius,radius+y+1):
                    possible_points.append((i,j))

            #cir_area = pie r ^2

            #check if triangle is bigger than radius
            for tup in possible_points:
                long_side = ((tup[0]-x)**2 + (tup[1]-y)**2) ** .5
                if long_side <= radius:
                    result.add((tup[0],tup[1]))

        return len(result)

        
test = Solution()
print(test.countLatticePoints([[2,2,1]]))