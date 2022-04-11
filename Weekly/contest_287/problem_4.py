class Encrypter:

    def __init__(self, keys, values, dictionary):
        self.keys = keys
        self.values = values
        self.dictionary = dictionary
        

    def encrypt(self, word1: str) -> str:
        list_word1 = list(word1)
        for char in word1:
            #find the index in keys
            idx = self.keys.index(char)
            list_word1[idx] = self.values[idx]
        return "".join(list_word1)

    def decrypt(self, word2: str) -> int:
        result = []
        list_word2 = list(word2)
        possible_strings = []
        completed_strings = set()
        for i in range(0,len(list_word2),2):
            copy_values = self.values.copy()

            idx_list = []
            substring = word2[i:i+2]
            if substring not in completed_strings:
                idx_list = [idx for idx,val in enumerate(copy_values) if val == substring]
                temp = []
                for idx in idx_list:
                    temp.append(self.keys[idx])
                possible_strings.append(temp)
                completed_strings.add(substring)
            # idx = self.copy_values.index(substring)
            # decrypted_substring = self.keys[idx]
            # list_word2[0] = decrypted_substring[0]
            # list_word2[1] = ''
        count = 0

        for li in possible_strings:
            result.append(''.join(li))
        for word in self.dictionary:
            check = False
            for element in result:
                if element not in word:
                    check = True
            if check == False:
                count += 1


        return count
        

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
test = Encrypter(['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"],["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
#print(test.encrypt('abcd'))
print(test.decrypt('eizfeiam'))
