# Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

# A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

class Solution:
    def kthPalindrome(self, queries, intLength: int):
        
        min_number = min(queries)
        max_number = max(queries)

        start = 1 + '0' * intLength
        start = int(start)

        