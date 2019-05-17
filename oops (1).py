#Class --- Blueprint of an object is calledd class..
#Object -- Instance of a class..


#class  - is the keyword for defining a class.

# class Classname:
	# statement
# Classname is recommended to stat with uppercase character.

# Student
# student

# class First:
# 	a=78
# 	b=76
# 	print(a+b)

# def add():
# 	a=56
# 	b=67
# 	print(a+b)

# obj=First()
# print(obj.a)
# print(First.a)

# class First:
# 	a=78
# 	b=76  #class Attrb
# 	# print(a+b)
# 	def add(self,c,d): #instance attributes
# 		print(c)
# 		print(d)
# 		print(self.a)
# 		print(self.b)
# 		return self.a+self.b

# # print(First.add())

# obj1=First()
# print(obj1.add(5,3))



# Constructor

# __init__ -- magic method

# __init__.py  -- Converting Folders into packages

# class Student:
# 	std_name="venkatesh"  #class Attribute
# 	def __init__(self,std_name,std_mobile):#instance methods
# 		self.std_name=std_name #instance attributes
# 		print("{} mobile number is {}".format(std_name,std_mobile))

# obj2=Student("ramesh",'728892382')

# print(Student.std_name)
# print(obj2.std_name)

#__init__ -- method will not return any output .. it will return None itself.



# Methods -- 

	# 1)Instance Method -- which will be called only using object..
	# 2)Class Method -- which will be called only using Class.
	# 3)Static Method -- which will be called with both obj and class.

# "pavanchogle@gmail.com"