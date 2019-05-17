# 1)instance method  - Method which contains self as the default arguments and 
# can be accessed only using object...


# class Student:

# 	def __init__(self,name,email):
# 		self.name=name
# 		print(name)

# 	def course(self,course):
# 		return "{} is taking {} course".format(self.name,course)

# obj=Student('venkat','venkat@gmail.com')
# print(obj.name)
# print(obj.course("python"))
# print(Student.course('python'))


#class methods-- Method which contains cls as default argument and can be accessed
# with both class and object...


# class Student:
# 	def __init__(self,name,email):
# 		self.name=name
# 		print(name)

# 	@classmethod
# 	def coursedetails(cls,name,course):
# 		cls.name=name
# 		return "{} is taking {} course".format(name,course)

# 	@classmethod
# 	def std_details(cls,mobile):
# 		return "{} has {} as mobile number".format(cls.name,mobile)

# obj=Student('kumar','kumar@gmail.com')
# print(obj.name)
# print(obj.coursedetails('rajesh','django'))
# print(Student.coursedetails('rajesh','django'))
# print(Student.std_details('672828228'))

#static method -- Which will not tak any defalt arguments but can be accessed with
# both class and Object..

# class Student:
# 	def __init__(self,name,email):
# 		self.name=name
# 		print(name)

# 	@staticmethod
# 	def coursedetails(name,course):
# 		# cls.name=name
# 		return "{} is taking {} course".format(name,course)

# 	@staticmethod
# 	def std_details(name,mobile):
# 		return "{} has {} as mobile number".format(name,mobile)

# obj=Student('kumar','kumar@gmail.com')
# print(obj.name)
# print(obj.coursedetails('rajesh','django'))
# print(Student.coursedetails('rajesh','django'))
# print(Student.std_details('rajesh','672828228'))


