#Fileoperation -- Those operation we ca d on a file..(read,write,append)


#read - r
#write - w
#append - a


#open a file..


# open() -- it is the function to open a file..


# file=open('sample.txt','r')

# #read()
# #readline()
# #readlines()

# for i in file.read():
# 	print(i)

# file.close()

# with open('C:/Users/Digitallync/Documents/sample.txt','r') as file:
# 	# print(file.read())
# 	# print(file.readline())
# 	# print(file.readline())
# 	# for line in file.readlines():
# 	# 	if 'Python' in line:
# 			# print(line)
# 	print([line for line in file.readlines()  if 'Python' in line ])

#wriiting-- It will remove all the previous and add th new content...

#write -- A single string at a time..
#writelines -- it will take list of elements where every element is a line in the file..
# with open('C:/Users/Digitallync/Documents/sample1.txt','w') as file:
# 	# file.write('This is th first File opeeration comand.\nDatascieence uses Python writing the logicc faster and using inbuilt modules..\n')
# 	file.writelines(['This is th first File opeeration comand.\n','Datascieence uses Python writing the logicc faster and using inbuilt modules..\n','Python Programming\n'])

#append--  It will to the previous existing content..
	#write -- A single string at a time..
	#writelines -- it will take list of elements where every element is a line in the file..

# with open('C:/Users/Digitallync/Documents/sample1.txt','a') as file:
# 	# file.write('This is th first File opeeration comand.\nDatascieence uses Python writing the logicc faster and using inbuilt modules..\n')
# 	file.seek(0,2)
# 	print(file.tell())
# 	# file.seek(0,2)
# 	file.write('Helloworld')
	# print(file.tell())
	# file.writelines(['This is th first File opeeration comand.\n','Datascieence uses Python writing the logicc faster and using inbuilt modules..\n','Python Programming\n'])
	# print(file.tell())
	# file.seek(0,0)
	# print(file.tell())


# CSV file functionlity...

# import csv

# with open('sample.csv','r') as file:
# 	for row in csv.reader(file):
# 		if 'ramesh' in row:
# 			print(row)

