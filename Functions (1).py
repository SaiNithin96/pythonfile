# Functions -- Code reusability..(repetition of code will be reduced..)

# def -- is the keyword for defining a functions..(declaration)

"""Syntax
def finctionname():
	statements
"""


# def add():
# 	print(4+3)

# # Calling a Functions
# # with out calling the functions the statements inside the defined functions wll not be executed.

# add()
# add()

#Passing the Arguments to the functions.....

#1)Default Arguments
#2)Positional Arguments
#3)Keyword Arguments
#4)Arbitrary Positional Arguments
#5)Arbitrary Keyword Arguments

#2)Positional Arguments

# def add(a,b):
# 	print(a)
# 	print(b)
# 	print(a+b)

# add(4,3)
# add(10,9)

#1) Default Arguments:

# def add(b=9,a=5):
# 	print(a)
# 	print(b)
# 	print(a+b)

# add()
# add(10,7)

# NOTE:- Once a defualt argument is declared after that all arguments should be 
# default aruments only at function declaration...


# 3)Keyword Arguments ::--

# NOTE:- Once a keyword argument is declared after that all arguments should be 
# keyword aruments only at function calling...

# def add(a,b,c,d):
# 	print(a)
# 	print(b)
# 	print(c)
# 	print(d)
# 	print((a+b)*(c-d))

# # add(2,3,4,5)
# # add(2,5,d=6,c=7)
# add(b=5,a=2,d=6,c=7)



#4) Arbitrary Positional Arguments

# When you dont know how many positional arguments that you will pass at the fucntion call.

def add(*b):
	print(b)
	c=0
	for j in b:
		# print(j)
		# c=c+j
		c+=j
	print(c)
add(3,4)
add(4,5,6)
add(6,7,8,9) 

