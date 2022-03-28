class Node:
   def __init__(self,data):
      self.data=data
      self.next=None
class linked:
   def __init__(self):
      self.head=None
   def print(self):
      temp=self.head
      while temp.next:
         print(temp.data)
         temp=temp.next
   def middle(self):
      counter=0
      position=0
      temp=self.head
      while temp.next:
         counter+=1
         temp=temp.next
      
      counter=counter//2
      while temp.next:
         position+=1
         if counter==position:
            return temp.data
         temp=temp.next
   def push(self,data):
      newnode=Node(data)
      newnode.next=self.head
      self.head=newnode

llist=linked()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)
print("the elements are ")
llist.print()
print("the middle element is ")
print(llist.middle())
      