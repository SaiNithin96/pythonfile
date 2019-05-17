# Datahiding or Encapsulation --- Restricting the acces to variables or methods..

# class Student:
# 	a=56 #(Public variables) # Those which can be accessed in or outside of class with out any restrictions.
# 	__b=76 #Private Varibales # Those cannot be accessed outside of the class.
	
# 	def add(self): #public 
# 		return self.a+self.__b

# 	def __sub(self): #private method
# 		return self.__b-self.a

# obj=Student()
# print(obj.add())
# print(obj.a)
# # print(obj.__b)
# # print(obj.__sub())

# # accessing ptivate varibales

# print(obj._Student__b)
# print(obj._Student__sub())



# #Method Overriding

# class First:
# 	a=5
# 	b=6
# 	def add(self):
# 		return self.a+self.b


# class Second(First):
# 	a=67
# 	b=67

# 	def add(self):
# 		return self.a-self.b

# obj=Second()
# print(obj.add())

# Both Method Overriding and Overloading Comes under POLYMORPHISM

