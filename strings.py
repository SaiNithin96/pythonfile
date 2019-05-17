# String -- Sequence of character or number or special symbols which are declared inside " " or ' ' or """ """...


a='python is the best programming language"s'
b='python'

# print(a)
# print(b)

# String declared with " " or ' ' is called as single line strings...

#String delcared with """ """ is called as multipleline strings..

c="""Hyderabad
is the captial 
of Telanagana"""

# print(c)

# Mutable-- Those variables where we can make changes .....(list,dictionary,set)
# Immutable -- Those values or variables where we cannot make changes --(string,tuple,numbers)


# ****Strings are Immutable ****

# Accessing value inside the string -- (Indexing)...

a="dhoni captian of csk"

# Positive Indexing will start form zero..

# print(a[15])
# print(a[12])

# Accessing Range of values

# print(a[3:13])

# print(a[5:16])


#Slicing-- specifying the jump arguments...

# 3 5 7 9 11
# print(a[3:13:2])

#negative indexing -- Accessing from right to left by specifying negative index values..

#Negativ indexing will start form  -1......
# a="dhoni captian of csk"

# # print(a[-5])
# # print(a[-12])

# print(a[-5:-15])

# # We cannot access range of elements using negative indexing..(by specifying 2 arguments)

# print(a[-5:-15:-1])



# Immutable --


# a="python"
# # a[3]="j"
# del a[3]
# print(a[3])

#Basic Operations
	#1)Concatenation (+)-- adding of multiple strings..
	#2)Repetition (*)  -- repeating the same string multile times..
	


# print("Hyderabad" + "Amaravathi")#concatenation

# print('23'+'24')


# print("csk"*4)#repetition

#string Methods

"""startswith,endswith,isalpha,isalnum,isdigit,islower,isupper,lower,upper,swapcase,title
capitalize,len,index,find,count,strip,lstrip,rstrip,split,join,replace,zfill"""

# print(help(str))
# print(dir(str))


# a="Delhi captial of India " #main string

# b="del" #substring
# #startswith -- It will check whether main string is starting with the specified substring..(Output will be Boolean(True/False))
# c='dia '
# print(a.startswith(b))

#endswith -- It will check whether main string is ending with specifed sub string..

# print(a.endswith(c))

d="Datascinceusespythonastheprog5151515raminglanguage"

#isalpha -- it will whether everything inside the string is alphabets only(lower or uppercase)..
#(True/False)

# print(d.isalpha())

# isalnum -- it will whether everything inside the string is alphabets or numbers only(lower or uppercase)..
#(True/False)

# print(d.isalnum())

# isdigit -- it will whether everything inside the string is numbers only..
#(True/False)

# e="56565111"
# # print(d.isdigit())
# print(e.isdigit())


# f="PYTHON123$##"
# # islower() -- All the alphabets inside the string should be in lower case..

# print(f.islower())

# # isupper() -- All the alphabets inside the string should be in upper case..

# print(f.isupper())

# g="Kohli highest ruNgetter in IPL"

#lower  -- convert all the alphabets inside the string into lowwercase..

# print(g.lower())

# print(id(g))
# print(id(g.lower()))

#upper  -- convert all the alphabets inside the string ino Uppercase...

# print(g.upper())

# g="Kohli highest ruNgetter in IPL"


# swapcase -- Convert lowercase to uppercase and vicversa in the string..

# print(g.swapcase())

# title -- convert starting caharacter of each word in the string will be converted into Uppercase.

# print(g.title())

# # capitalize -- Convert only starting characters of the string into uppercase..

# print(g.capitalize())

# len - - will return the length of that particular string..

# print(len(g))

g="Kohli highest ruNgetester ruNin IPL"

# index -- will return the index value of specified substring in the main string which will return only starting substing index..

# print(g.index('ruN'))
# print(g.find('ruN'))

# find -- will return the index value of specified substring in the main string which will return only starting substing index..

#difference between find and index.../

#index will retunr error when substring not found. but find will retunr -1 when sbstring not there.

# print(g.index('run'))
# print(g.find('run'))


# count -- will retunr how many times particular substring is repeated in the main string.

# print(g.count('es'))


# strip()  -- 

# a="\n\tdhoni the captian \n\t CSK\n\t"

# print(a)

# print(a.strip()) # it will remove the esape squence at the startng and ending of the string.

# print(a.strip('a'))

# print(a.lstrip())
# print(a.rstrip())

# split() -- It will split the string based on the condition we specified if your not going
# to specify it will defaultly do by using space...

		#Output will be in the format of list... 

# a="Assembly1polling1was1done1yestreday"

# print(a.split())

# print(a.split('1'))


# replace -- It will replace a substring in the main string with our specified string all the 
#occurence in the string..

# a="programminglanguage"

# print((a.replace('g','j')))
# print((a.replace('g','j',2)))
# print((a))

#zfill -- it will fill with 0's at the starting in the string if the lenght of string is 
# lessthan the specified condition..


# a="888383737388292929"

# print(a.zfill(15))


#join -- it will join the multiple elements as single string..
	#It will work only for string type values...


# a=('a','b','c','d','e')

# print("1".join(a))


# a=['f','b']
# b=['c','d','e']

# # print("".join(a,b))


# c=""

# for i in a:
# 	# print(i)
# 	# i+c
# 	# print(c)
# 	c=c+i
# 	# print(c)
# 	# print(i+"")
# print(c)

# for j in b:
# 	print(c)
# 	c=c+j 
# 	print(c)

# print(c)



















