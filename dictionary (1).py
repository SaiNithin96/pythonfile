# Dictionary -- sequence of Key:value pair seperated with comma(,) declared inside { }..

#Ex:- a={'game':'cricket','teams':['csk','rcb','kkr','srh'],'game':'football'}

# Every Key should be unique...
c=[1,2,2,3]
a={'game':'cricket','teams':['csk','rcb','kkr','srh'],'game':'football','data':c}

print(a)


# All the keys should be immutables...

# Values can be of any datatypes..

# b={'1':'python',1:'django',(3,4,5):'datascience',[6,7,8]:'devops'}

# print(b)

# Dictionary are Mutuable data types . we can make changes inside the dictionary..


# Accessing inside the ddictionary..


# print(a['teams'][3])

# print(a['1'])

#get -- it will return the values associated with that particular key if the key is present or else retunr None.

# print(a.get('teams'))

# print(a.get('1'))


# Adding and Updating Key Values into the Dictionary..

a={'game':'cricket','teams':['csk','rcb','kkr','srh'],'game':'football','data':c}

# a['game']='kabaddi'
# a['game1']='kabaddi'


b={'trophy':['Wcc','Ipl','BBL'],'captains':['MSD','Kohli','Dinesh']}

# print(a)

# # Update  -- It is used for adding 2 Dictionary..

a.update(b)

# print(a)

# Deleting Key:Value from the dictinary..

# del a['trophy']

# print(a)

#pop,popitem,clear

#clear -- making it as empty dictionary removing all the key:value from the dictionary..

# a.clear()
# print(a)

# pop -- remove the key:vaue pair based on the key provided and will return values removed..


# print(a.pop('trophy'))

# print(a)

#popitem() - It will remove the last Key:value pair we have and retunr the removed key:value

# print(a.popitem())

# print(a)


# keys -- It will return all the keysinside the dictionry..


a={'game':'cricket','teams':['csk','rcb','kkr','srh'],'game':'football','data':'1','trophy':['Wcc','Ipl','BBL'],'captains':['MSD','Kohli','Dinesh']}


# print(a.keys())


# values -- It will return all the values inside the dictionary..

# print(a.values())


# items  -- It will return (key,values) pair in a tuple..

# print(a.items())

# print(dir(dict))


# copy -- takes values as the reference and create a new location for the values..

# a={'game':'cricket','teams':['csk','rcb','kkr','srh'],'game':'football','data':'1','trophy':['Wcc','Ipl','BBL'],'captains':['MSD','Kohli','Dinesh']}

# b=a

# # print(a)
# # print(b)

# # b['data1']="2"

# # print(id(b))
# # print(id(a))


# b=a.copy()

# print(id(a))
# print(id(b))

# b['data1']="2"

# print(a)

# print(b)


# fromkeys -- It will take the iterables and will consider each element as key in the dictioary
# and value will be None if we not provide else value we provided..

# print(help(dict))

# a={}
# print(a.fromkeys('abc',['python','django']))

# print(a)

# setdefault -- Providding a default value for the key inside the dictinary..


# a.setdefault('data','hyderabad')

# print(a)


a={1:1,2:4,3:9,4:16,5:25,6:36}
# # print(a)
# # a[7]=49
# # print(a)
# b={}
# c={}
# # print(a[4])

# for j in a:
# 	if j%2==0:
# 		pass
# 		# print(a[j])
# 		b[j]=a[j]
# 	else:
# 		c[j]=a[j]
# print(b)
# print(c)

# Dictionary Comprehension

# print({x:x**2 for x in range(1,7) if x%2==1})

# print({x:x**2 if x%2==0 else x**3 for x in range(1,7)})