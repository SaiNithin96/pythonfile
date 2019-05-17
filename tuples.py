# Tuple -- Sequece of elements which are separated with comma(,) declared inside parenthesis( )..

# Ex:- a=(3,7.6,'programming',[2,3,4,5],(7,8,9))

# Tuples elements are immutable...(we cannot make changes inside the tuples..)

# a=3,7.6,'programming',[2,3,4,5],(7,8,9)

b=(3,7.6,'programming',[2,3,4,5],(7,8,9))


# print(type(a))
# print(type(b))

# print(a)

# c=(4,)

# print(type(c))

# Accessing element inside the tuple is same as List and Strings..


# print(b[4]) #indexing
# print(b[0:4]) #idexing
# print(b[0:5:2]) #slicing

# b[1]=15.8

# del b[1]


# Basic Operatins
	#concatenation(+)
	#repetition(*)

# print((1,2,3)+('a','b','c'))

# print((1,2,3)*3)
# #Methods inside tuples are (len,index,count)

# b=(3,7.6,'programming',[2,3,4,5],(7,8,9))


# # b[3].append(6)

# print(b)

# print(len(b))
# print(b.index(3))
# print(b.count('a'))


a=(1,2,3,4,5,6,7,8,9)

b=()
c=()

for j in a:
	if j%2==0:
		b=b+(j,)
		# print(id(j))
		# print(j)
	else:
		c=c+(j,)
		# print(j)

# print(b)
# print(c)

# Tuple Comprehension:-
 
	#syntax :-   (j for j in a)
				#(j for j in a if j%2==0)
				#(j if j%2==0 else j+5 for j in a)


# print(tuple(j for j in a)) #(1,2,3,4,5,6,7,8,9)
# print(tuple(j for j in a if j%2==0))   #(2,4,6,8)

# print(tuple(j if j%2==0 else j+5 for j in a)) #(6,2,8,4,10,6,12,8,14)

