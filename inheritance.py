#Inheritance -- A class getting the properties from its super class..

#child class getting the properties form parent..


# 3 types of Inheritance:
	#1) Single Inheritance --
	#2) Multiple Inheritance --
	#3) Multilevel Inheritance --


class Employee:
	name="Suresh" #class Attribute
	designation="Developer"
	def __init__(self,name):
		self.name=Employee.name

class Details(Employee):
	# name="Naresh"
	def __init__(self,name):
		# self.name=name
		print(self.name)

obj=Details('Naresh')
print(obj.name)