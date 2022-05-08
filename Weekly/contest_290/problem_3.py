from cmath import rect

from collections import defaultdict
class Solution:
    def countRectangles(self, rectangles, points):
        #hash_rec = {i:set() for i in range(len(rectangles))}
        hash_rec = {i:[] for i in range(len(rectangles))}
        
        for i in range(len(rectangles)):
            #rectangles[i]
            
            #get all points within rectangle
            # for x in range(0,rectangles[i][0]+1):
            #     for y in range(0,rectangles[i][1]+1):
            #         hash_rec[i].add((x,y))
            hash_rec[i] = [rectangles[i][0],rectangles[i][1]]


        #get max x and y from hashmap
        max_x,max_y = 0,0


        for key,val in hash_rec.items():
            temp_x = val[0]
            temp_y = val[1]
            max_x = max(temp_x,max_x)
            max_y = max(temp_y,max_y)


        final_hash_x = {x:0 for x in range(max_x+1)}
        final_hash_y = {y:0 for y in range(max_y+1)}



        for val in hash_rec.values():
            x = val[0]
            y = val[1]

            for key,val in final_hash_x.items():
                if key <= x:
                    final_hash_x[key] += 1

            for key,val in final_hash_y.items():
                if key <= y:
                    final_hash_y[key] += 1
        
        

        
        result = []
        for point in points:
            x,y = point[0],point[1]

            # for key,val in hash_rec.items():
            #     #if (x,y) in val:
            #     if x <= val[0] and y<= val[1]:
            #         count += 1

            count = min(final_hash_x[x],final_hash_y[y])

            result.append(count)
        
        return result


test = Solution()
# print(test.countRectangles([[1,2],[2,3],[2,5]],[[2,1],[1,4]]))
# print(test.countRectangles([[1,1],[2,2],[3,3]],[[1,3],[1,1]]))

print(test.countRectangles([[4,7],[4,9],[8,5],[6,2],[6,4]],[[4,2],[5,6]]))
        
