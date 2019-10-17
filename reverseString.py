class Solution:
    def reverseString(self, s):
        if len(s) <=1:
            return s
        # return s[-1::-1]
        words= s.split(" ")
        new_string=[]
        for word in words:
            new_string.insert(0, word) #--[mom]<--[my]<--[love]<--[ I]

        return " ".join(new_string)



#O(N): Time and O(1): Space 
print(Solution().reverseString(" I love my mom "))
