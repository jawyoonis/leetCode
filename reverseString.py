class Solution:
    def reverseString(self, s):
        if len(s) <=1:
            return s
        words= s.split(" ")
        new_string=[]
        for word in words:
            new_string.insert(0, word) #--[mom]<--[my]<--[love]<--[ I]

        return " ".join(new_string)




print(Solution().reverseString(" I love my mom "))
