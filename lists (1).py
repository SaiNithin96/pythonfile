# List -- Sequence of elements which are declared inside [ ] seperated with comma(,)..

#elements -- numbers,string,list

# Ex:- a = [4.5,6,'abc',[8,9,0]]

# Lists are Mutuable..(Making chhanges inside the list is possible..)

a=[4.5,6,'abc',[8,9,0],23,'python',67.4,'programming']

# print(a)

# print(a[3]) #indexing

# print(a[0:3]) #indexing

# print(a[0:8:2]) # slicing


# print(a[-1])

# print(a[-6])

# print(a[-1:-7:-2]) #negative indexing


# Basic Operations

# concatenation (+) -- Add multiple list into single list
# repetition (*) - Repeting element inside the list multiple number of times..

# print([1,2,3,4]+[4,5,6,7]+[7,8,9,0])

#Output -- [1,2,3,4,4,5,6,7,7,8,9,0]

# print([3,4,5,6]*2)

#Output -- [3,4,5,6,3,4,5,6]


# a=[1,2,56,45,'python',76.5]

# a[2]='programming'

# print(a)

# del a[3]

# print(a)

# #List Methods
# """append , extend , insert, remove, pop,clear, sort,reverse, index, count, len,copy"""
# # print(dir(list))


# #append -- it is used for adding a single element at last in the list..


# a=[4,'cricket',68.34]

# a.append('5')
# print(a)

# # a.append('6',7)

# a.append(['6',7])
# print(a)

# # extend -- for adding mutiple elements into the list..(it will take only iterable)


# a.extend([3,4,5])

# print(a)
# b='csk is good team'.split()
# # a.extend(['csk',['csk','is']])
# a.extend(b)
# print(a)

# # insert -- for adding an elemnt at the particular index inside the list(single element). 
# a.insert(2,'python')

# print(a)

# # remove -- remove and element based on the value specified..

# # a.remove('4')

# # print(a)

# # print(type(a.pop(4)))

# # print(a)

# # a.clear()
# # print(a)



# # print(a.index('csk'))

# # print(len(a))

# # print(a.count(4))

# # for i in a:
# # 	if type(i)==list:
# # 		i.remove(7)

# # print(a)
# a=[56,4,5,6,63,759,34,54]

# # print(a.sort())
# # print(a)
# # a.sort(reverse=True)

# # print(a)


# reverse -- 
# print(a[::-1])
# print(a)

# a.reverse()
# print(a)


# copy -- 



a=[1,2,3,4,5]


# b=a


# print(a)
# print(b)

# print(id(a))
# print(id(b))

# b.append(6)

# print(b)
# print(a)


# b=a.copy()

# print(a)
# print(b)

# print(id(a))
# print(id(b))

# b.append(6)
# print(b)
# print(a)


a=[4,76,12,98,43,647,43,65,78]
# b=[]
# c=[]
# for j in a:
# 	if j%2==0:
# 		# print(j)
# 		b.append(j)
# 	else:
# 		# print(j,"is odd number")
# 		c.append(j)

# print(b)
# print(c)


# Syntax of List comprehensions

"""  [j for j in a]"""
"""  [j for j in a if j%2==0] """

# print([j for j in a])

# print([j for j in a if j%2==0])

# b=[j if j%2==0 else j+1 for j in a]
# print(b)

# a=['a','b','i','j','k','e','u']

# for j in a:
# 	if j in "aeiou":
# 		print(j)

# print([j for j in a if j in 'aeiou'])




