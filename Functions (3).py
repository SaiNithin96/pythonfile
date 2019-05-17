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

# def add(*b):
# 	print(b)
# 	c=0
# 	for j in b:
# 		# print(j)
# 		# c=c+j
# 		c+=j
# 	print(c)
# add(3,4)
# add(4,5,6)
# add(6,7,8,9) 


#5) Arbitrary Keyword Arguments

# These are declared using (**kwargs)..


# def add(**a):
# 	statements


# def add(**kwargs):
# 	print(kwargs)
# 	count=0
# 	for j in kwargs:
# 		# print(kwargs[j])
# 		count=count+kwargs[j]
# 	print(count)

# add(a=3,b=5,c=7)
# add(d=1,e=4,f=8,g=9)
# add(q=12,r=13,s=14,t=15,u=16)


#Local and Global Variables in functions..

# a=23  #global variables -- which are declared outside of th functions and can be accessed from any where.
# #through out the program...

# def sample(b,c):
# 	print(b) #local variables-- which are declared inside the funcitona and an be accessed only
# 	# inside the functions itself.

# 	print(c)
# 	print(a)
# sample(4,5)
# print(a)
# print(b)


# Return Statement -- Statement which will store some value and send it to the functions call.


# Once a return is reahced inside the functions the cursor will direclty move to where the 
# functions is called..

# def add(a,b,c):
# 	print(a)
# 	print(a+b+c)
# 	return a+b+c
# 	print(b)
# 	print(b)
# 	print(b)
# 	print(b)

# print(add(3,4,5))

# print(add(7,8,9))


# Recursion -- A function calling itself.

# 6! == 6*5*4*3*2*1 ==720


# def cal_fact(a):
# 	if a==1:
# 		return 1

# 	else:
# 		return a*cal_fact(a-1) #(6*5*4*3*2*1)

# print(cal_fact(int(input("Enter a value"))))
# # print(cal_fact(7))



# Lambda -- A functions which does not contains any name..


# def

#lambda -- is the keyword for declaring lambda functions..


# def fucntionname():
	# statement

#Syntax
	# lambda a:a*2

# print((lambda a:a*2)(2))
# c=lambda a,b:a*b
# print(c(2,3))
# print(c(4,6))

#map -- iteration
#filter --- condiitonal
#reduce -- Single output

