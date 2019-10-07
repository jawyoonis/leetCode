class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        ls = [' ','','abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = ['']
        for i in range(len(digits)):
            l2 = ls[int(digits[i])]
            ans = [a+b for a in ans for b in l2]

	return (ans)
print Solution().letterCombinations("23")
