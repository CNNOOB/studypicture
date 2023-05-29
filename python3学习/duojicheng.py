class people:
    name=''
    age=0
    __weight=0
    def __init__(self,n,a,w):
         self.name=n
         self.age=a
         self.__weight=w
    def speak(self):
        print("{0}说: 我 {1} 岁。".format(self.name,self.age))

class student(people):
	grade=''
	def __init__(self,n,a,w,g):
		people.__init__(self,n,a,w)
		self.grade=g
	def speak(self):
		print("{0}说：我{1}岁了，我在读{2}年级")

class speaker():
	topic=''
	name=''
	def __init__(self,n,t):
		self.name=n
		self.topic=t
	def speak(self):
		print("我叫{0}，我是一个演说家，我演说的主体是{1}".format(self.name,self.topic))

class sample(speaker,student):
	def __init__(self,n,a,w,g,t):
		student.__init__(self,n,a,w,g)
		speaker.__init__(self,n,t)
test = sample("Tim",25,80,4,"Python")
test.speak()