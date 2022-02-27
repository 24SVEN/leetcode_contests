#https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        smaller_string,larger_string = '',''

        

        if len(s)> len(t):
            smaller_string = s
            larger_string = t
        else:
            larger_string = s
            smaller_string = t

        count = 0
        large_string_count = len(larger_string)
        #find missing characters from smaller and larger
        #guess find larger first

        ld = {}
        sd = {}

        #convert strings to dictionaries
        for char in larger_string:
            if char in ld:
                ld[char] += 1
            else:
                ld[char] = 1
        

        for char in smaller_string:
            if char in sd:
                sd[char] += 1
            else:
                sd[char] = 1

        for char in smaller_string:
            if char in ld:
                ld[char] -= 1
                if ld[char] == 0:
                    del ld[char]
            else:
                count += 1

        

        diff = large_string_count + count - len(smaller_string)
        count = diff+ count
        print(count)
        return count

test = Solution()
test.minSteps('leetcode','coats')
test.minSteps('night','thing')
