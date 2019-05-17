# Lambda functions -- a functions with any name..



# Syntax:


# c=lambda a,b:a+b
# print(c(5,6))

# def add(a,b):
	# return a+b

d=[2,3,'4',5,'6',7,'8',9]

#map --- 

# print(list(map(lambda j:j*3,d)))
# print(tuple(map(lambda j:j*3,d)))


# def mul(d):
# 	e=[]
# 	for j in d:
# 		# print(j*3)
# 		e.append(j*3)
# 	return e
# print(mul(d))


# filter -- 

# print(list(filter(lambda j:type(j)==str,d)))

e=range(2,15)
# reduce 

import functools

# [2,3,4,5,6,7,8,9,10,11,12,13,14]
# print(functools.reduce(lambda a,b:a+b,e)) #a=2,b=3

f=[45,12,6,72,78,14,104,253,32]

print(functools.reduce(lambda a,b:a if a>b else b,f))