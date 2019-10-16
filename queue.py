class Queue(object):
    def __init__(self):
        self.stack1=[]
        self.stack2=[]



    def enqueue(self, element):
        self.stack1.append(element)




    def dequeue(self):
        if len(self.stack2)==0:
            if len(self.stack1)==0:
                return
            while len(self.stack1)> 0:
                new_element= self.stack1.pop()
                self.stack2.append(new_element)
        return self.stack2



q= Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
