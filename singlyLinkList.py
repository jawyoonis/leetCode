class Node:
  def __init__(self, data):
    self.data=data 
    self.next=None


class SinglyLinkList:
  def __init__(self):
    self.head=None




  def append(self, data):
    new_node= Node(data)

    if self.head==None:
      self.head=new_node 
      return 

    last_node= self.head 
    while last_node.next:
      last_node=last_node.next
    last_node.next= new_node 


  def print(self):
    cur_node=self.head 

    while cur_node:
      print(cur_node.data)
      cur_node= cur_node.next

 


llist =SinglyLinkList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")



llist.print()

