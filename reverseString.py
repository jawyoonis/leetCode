# class Solution:
#     def reverseString(self, s):
#         if len(s) <=1:
#             return s
#         # return s[-1::-1]
#         words= s.split(" ")
#         new_string=[]
#         for word in words:
#             new_string.insert(0, word) #--[mom]<--[my]<--[love]<--[ I]

#         return " ".join(new_string)



# #O(N): Time and O(1): Space 
# print(Solution().reverseString(" I love my mom "))




#reverse string using stack 


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items






def reverseString(strings, stack ):
  for i in range(len(strings)):
    stack.push(strings[i])

  reverse=''
  while not stack.is_empty():
    reverse+=stack.pop()
  return reverse 






  s= Stack()

  print(s.reverseString("hello", s))



