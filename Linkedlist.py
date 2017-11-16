class Linkedlist:
  def __init__(self):	  
    self.head=None
    self.tail=None
    self.count=0

  def addnode(self,data):
  	temp = Node(data)
  	temp.setnext(self.head)
  	self.head=temp
  	self.count+=1
  	
  
  def shownodes(self):
  	print('\n')
  	for i in range(0,self.count):
  	  print('->',+self.head.getdata(),end=' ')
  	  self.head=self.head.getnext()
    print('\n')

class Node:
	def __init__(self,data=None):
	   self.data = data
	   self.next=None

	def getdata(self):
	   #print(self.data)
	   return self.data

	
	def setdata(self,data):
	   self.data=data

	def getnext(self):
	   return self.next 


	def setnext(self,next):
	   self.next=next

ll= Linkedlist()
a1=int(input());a2=int(input());a3=int(input());a4=int(input());a5=int(input())
ll.addnode(a1);ll.addnode(a2);ll.addnode(a3);ll.addnode(a4);ll.addnode(a5)
ll.shownodes()