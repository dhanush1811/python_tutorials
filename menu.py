class menu:
  d={}
	def add(self,name,price):
		self.d[name]=price
	def show(self):
		print(self.d)

m=menu()
m.add("idly",10)
m.add("vada",20)
m.show() 
