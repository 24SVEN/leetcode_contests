import string
class Solution:
    def cellsInRange(self, s: str):


        first_num = int(s[1])
        second_num = int(s[4])

        result = []

        alphabet = [x for x in string.ascii_letters]
        

        first_char_idx = alphabet.index(s[0])
        second_char_idx = alphabet.index(s[3])

        for col in range(first_char_idx,second_char_idx + 1):
            for row in range(first_num,second_num+1):
                result.append(alphabet[col] + str(row))

        return result



test = Solution()
print(test.cellsInRange("K1:L2"))
print(test.cellsInRange("A1:F1"))